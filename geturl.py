# coding:utf-8
import re
import requests
# 获取网页内容
where = 'http://www.glzy8.com/zt/excel/'
webaddr = "http://www.glzy8.com"
#print(where)
r = requests.get('http://www.glzy8.com/zt/excel/index.html')
data = r.text
f = open("url.txt","w")
f2 = open("url2.txt","w")
# 利用正则查找所有连接
link_list =re.findall(r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')" ,data)
for url in link_list:
	if ".html" in url :
		if len(url)==8 :
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
				if "rar&y=zt01" in url2 :
#					print(url2)
					print(url2,file=f2)
					r3 = requests.get(webaddr+url2)
					with open(url2[35:51:]+".rar",'wb') as f3:
					    f3.write(r3.content)
f.close()
f2.close()
