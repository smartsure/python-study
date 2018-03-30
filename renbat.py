
import os
#1获取重命名的文件夹
#folder_name = input('请输入文件夹的名字：')
folder_name= "F:\BaiduNetdiskDownload\excel"
#2获取文件夹中的文件名
file_names = os.listdir(folder_name)

print(type(file_names))

'''方法一
os.chdir(folder_name)
#3对获取的名字重命名
for name in file_names:
      print(name)
      os.rename(name,'[mittake出品]-'+name)'''

for name in file_names:
	print(name)
	old_file_name = folder_name + '\\' + name
	new_file_name = folder_name + '\\' + name[23::]
	os.rename(old_file_name,new_file_name)



