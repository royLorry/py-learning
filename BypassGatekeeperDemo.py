import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    "Connection": "keep-alive",
}

# Open gatekeeper page(RU shadow site) first
# Save the cookies
# Get a token named CSRFToken on this page
resGatekeeperPage = requests.get("https://www.lenovo.com/ru/ru/rushadow/gatekeeper/showpage?toggle=PasscodeGatekeeper", headers=headers) 
cookies = resGatekeeperPage.cookies.get_dict()
domGatekeeperPage = BeautifulSoup(resGatekeeperPage.text, "lxml")
CSRFToken = domGatekeeperPage.select("input[name=CSRFToken]")[0].get("value")

# Your passcode
PASSCODE = "EAST"
# Post below 3 parameters to /authGatekeeper API to bypass the Gatekeeper, do not forget to bring your cookies
payload = {'gatekeeperType': 'PasscodeGatekeeper', 'passcode': PASSCODE, 'CSRFToken':CSRFToken}
requests.post("https://www.lenovo.com/ru/ru/rushadow/gatekeeper/authGatekeeper", headers=headers, data=payload, cookies=cookies)

# Now you can open any page on RU shadow site with the cookies
resRUShadowHomepage = requests.get("https://www.lenovo.com/ru/ru/rushadow/", headers=headers, cookies=cookies)
domRUShadowHomepage = BeautifulSoup(resRUShadowHomepage.text, "lxml")
print(domRUShadowHomepage.title)