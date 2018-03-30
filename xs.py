def printMenu():
	#1 打印功能
	print("学生管理系统".center(30))
	print("*"*30)
	print("1.添加学生信息")
	print("2.修改学生信息")
	print("3.删除学生信息")
	print("4.查询学生信息")
	print("5.退出管理系统")
	print("*"*30)

def addStuInfo():
	newInfo={}
	newName=input("请输入学生的姓名:")
	newSex=input("请输入学生的性别:")
	newPhone=input("请输入学生的手机:")
	newInfo["name"]=newName
	newInfo["sex"]=newSex
	newInfo["phone"]=newPhone
	stuInfos.append(newInfo)	

def getStuInfo():
	newName=input("请输入学生的姓名:")
	newSex=input("请输入学生的性别:")
	newPhone=input("请输入学生的手机:")
	return newName,newSex,newPhone

stuInfos=[]

def main():
	while True :
		printMenu()

		key=input("\n选择：")

		if key=='1' :
			addStuInfo()
			print(stuInfos)
		elif key=='2' :
			stuId=int(input("请输入学生的序号:"))
			result=getStuInfo()
			stuInfos[stuId-1]["name"]=result[0]
			stuInfos[stuId-1]["sex"]=result[1]
			stuInfos[stuId-1]["phone"]=result[2]
			print("修改完成")
		elif key=='3' :
			stuId=int(input("请输入学生的序号:"))
			del stuInfos[stuId-1]
		elif key=='4' :
			print("*"*30)
			print("学生的信息如下:")
			print("*"*30)
			print("\n")
			print("序号	姓名	性别	手机号码")
			i=1
			for tempInfo in stuInfos :
				print("%d	%s	%s 	%s"%(i,tempInfo["name"],tempInfo["sex"],tempInfo["phone"]))
				i+=1
		elif key=='5' :
			break
		else :
			print("请输入正确选择：")

main()
