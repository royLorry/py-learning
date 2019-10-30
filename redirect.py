import requests
import xlrd
import xlwt

# print(r.history[i].url)
# print(r.history[i].elapsed.total_seconds())
# print(r.history[i].status_code)
# print(r.url)
# print(r.elapsed.total_seconds())
# print(r.status_code)

workbook = xlwt.Workbook(encoding = 'ascii')
worksheet = workbook.add_sheet('sheet1')
row = 1
worksheet.write(0, 0, label = "#")
worksheet.write(0, 1, label = "Original_URL")
worksheet.write(0, 2, label = "Redirects")
worksheet.write(0, 3, label = "Final_URL")

def get_redirect_path(url):
    global row
    headers = {
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding' : 'gzip, deflate, br',
    'Connection' : 'close',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
    r = requests.get(url, headers=headers)
    worksheet.write(row, 0, label = str(row))
    worksheet.write(row, 1, label = url)
    worksheet.write(row, 2, label = len(r.history))
    worksheet.write(row, 3, label = r.url)
    worksheet.write(row, 4, label = "Path:")
    k = 0
    for j in range(len(r.history)):
        worksheet.write(row, 5 + 2 * j, label = r.history[j].url)
        worksheet.write(row, 5 + 2 * j + 1, label = str(r.history[j].status_code)+" →")
        k += 1
    worksheet.write(row, 5 + 2 * k, label = r.url)
    row += 1

# data = xlrd.open_workbook('D:\\Desktop\\1.xls')
# table = data.sheet_by_index(0)
# for i in range(table.nrows):
#     try:
#         print(table.cell(i,0).value)
#         get_redirect_path(table.cell(i,0).value)
#     except:
#         worksheet.write(row, 0, label = str(row))
#         worksheet.write(row, 1, label = table.cell(i,0).value)
#         worksheet.write(row, 2, label = "Failed to load.")
#         row += 1
#         continue

get_redirect_path("https://www.lenovo.com/de/de/phones/moto/moto-z3-play/c/moto-z-series")

workbook.save('D:\\Desktop\\redirect_report0318.xls')


# get_redirect_path('http://www.lenovo.com/jp/ja/yoga/yoga-700-series/c/yoga-700-series')
# get_redirect_path('http://shop.lenovo.com/gh/en/events/')