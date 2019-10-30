import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    "Connection": "keep-alive",
}

# @param user_input
# @return pageSource
def getPageSource(user_input):
    # make an if condition to determine whether the user_input is a public site or closed site(with gatekeeper)
    resJudgementPage = requests.get(user_input, headers=headers, allow_redirects=False)
    resJudgementPageStatusCode = resJudgementPage.status_code
    if resJudgementPageStatusCode == 200:
        # 200 shows that user_input is a public site URL, we have got the source code, return it
        return BeautifulSoup(resJudgementPage.text, "lxml")
    elif resJudgementPageStatusCode == 302:
        # 302 shows that user_input is a closed site with gatekeeper, we have to login first and then return the source
        gatekeeperLoginPageURL = resJudgementPage.headers["Location"]
        resGatekeeperPage = requests.get(gatekeeperLoginPageURL, headers=headers)
        cookies = resGatekeeperPage.cookies.get_dict()
        domGatekeeperPage = BeautifulSoup(resGatekeeperPage.text, "lxml")
        CSRFToken = domGatekeeperPage.select("input[name=CSRFToken]")[0].get("value")
        gatekeeperLoginFormURL = "https://www.lenovo.com" + domGatekeeperPage.select("#nemoGatekeeperForm")[0].get("action")
        # Your passcode
        # TODO if we want login each sites, we need to record the passcode of each sites and make a switch judgment here. such as 'EAST' for E-EMEA sites
        PASSCODE = "nemo"
        # Post below 3 parameters to /authGatekeeper API to bypass the Gatekeeper, do not forget to bring your cookies
        payload = {'gatekeeperType': 'PasscodeGatekeeper', 'passcode': PASSCODE, 'CSRFToken':CSRFToken}
        requests.post(gatekeeperLoginFormURL, headers=headers, data=payload, cookies=cookies)
        resUserInputPage = requests.get(user_input, headers=headers, cookies=cookies)
        return BeautifulSoup(resUserInputPage.text, "lxml")
    else:
        # other unconsidered situations
        print(resJudgementPageStatusCode + " other unconsidered situations")
        return BeautifulSoup(resJudgementPage.text, "lxml")