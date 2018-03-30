# coding:utf-8
import os
import re
import requests
# 获取网页内容
where = 'https://pc.qq.com'
webaddr = "https://sm.myapp.com/original/Development/"
#print(where)
r = requests.get('https://pc.qq.com/category/c13.html')
data = r.text
f = open("soft.txt","w")
f2 = open("soft2.txt","w")
pathname="F:\BaiduNetdiskDownload\soft"
# 利用正则查找所有连接
link_list =re.findall(r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')" ,data)
for url in link_list:
	if "detail" in url :
#		if len(url)==8 :
			print(url,file=f)
#			print(type(url))
#			print(type(where))
#			print(where+url)
			r2 = requests.get(where+url)
			data2 = r2.text
#			print(len(data2))
#			print(type(data2))
			link_list2 = re.findall(r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')",data2)
			for url2 in link_list2 :
#				print(url2)
				if "https://sm" in url2 :
#					print(url2)
					print(url2,file=f2)
					r3 = requests.get(url2)
					filename=os.path.basename(url2)
					with open(pathname+"\\"+filename,'wb') as f3:
					    f3.write(r3.content)
f.close()
f2.close()
