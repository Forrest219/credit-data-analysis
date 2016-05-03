#  coding=utf-8
#
#  文件名:  comparingdata.py
#  功能:  输入两组文件数据，检查两者的差异，并输出。
#  作者：Forrest219

v1 = {0:0,1:1,2:2,4:4}
v2 = {0:1,1:1,2:1,3:3}

def comparingdata(data1, data2):

	result = [["ID", "data1_value", "data2_value", "comments"]]
	temp1 = []
	temp2 = []
	temp3 = []

	for key in data1:
		if key not in data2:
			temp1.append([key, data1[key], "", "item doesn't exist in data2"])
		elif data1[key]!=data2[key]:
			temp2.append([key, data1[key], data2[key], "item's value doesn't equal"])
		else:
			continue
	
	for key in data2:
		if key not in data1:
			temp3.append([key, "", data2[key], "item doesn't exist in data1"])
		else:
			continue
	result = result + temp1 + temp2 + temp3
	if len(result)==1:
		return "data1 and data2 is exactly the same!"
	else:
		return result

result = comparingdata(v1, v2)

#print(type(result))
#print(len(result))
for i in range(5):
	print(result[i])