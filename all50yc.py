# -*- coding: UTF-8 -*-
"""
Compatible for python2.x and python3.x
requirement: pip install requests
"""
from __future__ import print_function
import requests
import urllib
from lxml import etree
import time
import xlwt
import xlrd
import json
import numpy as np
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

if __name__ == "__main__":
	url = "https://www.50yc.com/"
	file = xlwt.Workbook(encoding = 'utf-8')
	sheet = file.add_sheet('test',cell_overwrite_ok=True )
	workbook = xlrd.open_workbook(r'D:\50yc.xls')
	read = workbook.sheet_by_index(0)
	headers = {
		  "Accept-Encoding": "gzip, deflate, br",
		  "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
		  "Accept-Language": "zh-CN,zh;q=0.9",
		  "Cache-Control":"max-age=0",
		  "Upgrade-Insecure-Requests":"1",
		  "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
		  "Host": "www.50yc.com",
		  "Origin": "https://www.50yc.com",
		  "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
		  "X-Requested-With":"XMLHttpRequest",
		  "Connection": "keep-alive"
		  }
	cookie = {
		  "mediav": "%7B%22eid%22%3A%22221573%22%2C%22ep%22%3A%22%22%2C%22vid%22%3A%22G%2FS'%3D2j-Z%25%3C!V*WrM%3AMr%22%2C%22ctn%22%3A%22%22%7D",
		  "50yc_SessionId": "1e213tclslrwd4cveahsoaqp",
		  "WLYC2":"ProvinceCode=110000&ProvincePinyin=beijing&ProvinceName=%e5%8c%97%e4%ba%ac&ConfigName=%e5%8c%97%e4%ba%ac%e5%b8%82",
		  "UM_distinctid":"165697da46173d-0528dc78de450f-323b5b03-100200-165697da462154",
		  "Qs_lvt_46053":"1535073168",
		  "Hm_lvt_f2adc225f77767e1753736cf746fd899":"1535073171",
		  "Hm_lvt_a7e92adec7077eb84d0b5bbd9ddab820":"1535073171",
		  "mediav":"%7B%22eid%22%3A%22221573%22%2C%22ep%22%3A%22%22%2C%22vid%22%3A%22G%2FS'%3D2j-Z%25%3C-x%3FZooPPK%22%2C%22ctn%22%3A%22%22%7D",
		  "CCKF_visitor_id_118905": "1117210535",
		  "CNZZDATA1256560111":"1168643603-1535068837-null%7C1535074241",
		  "cckf_track_118905_AutoInviteNumber":"0",
		  "cckf_track_118905_ManualInviteNumber":"0",
		  "Qs_pv_46053":"672810882917688300%2C3790273684511161300%2C3944790918233756700%2C950848723873419300%2C2740617612394151400",
		  "Hm_lpvt_f2adc225f77767e1753736cf746fd899":"1535077100",
		  "Hm_lpvt_a7e92adec7077eb84d0b5bbd9ddab820":"1535077100",
		  "cckf_track_118905_LastActiveTime":"1535077101"
		  }
	for i in range(0,1):
		url = url + str(read.cell_value(i,1)) + "/ov1"
		headers["Referer"] = url
		print(url)
		r = requests.get(url, headers=headers, cookies = cookie)
		tree=etree.HTML(r.content)
		sf =open('jackson.txt', 'wb')
		sf.write(r.text.encode('utf-8'))
		sf.close()
		nodes = tree.xpath("/descendant::div[@class='bg-hover']")
		for n in nodes:
			name = n.xpath("/descendant::p[@class='search-result-name']/strong")[0].text
			cid = n.xpath("/descendant::a[@class='searchlink']")[0].get('href')
			print(cid)