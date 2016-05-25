# -*- coding: utf-8 -*-
"""
Created on Wed May 25 09:01:32 2016

@author: Forrest219

Notes:
本脚本用于校验数据结构完全相同的两个文件的差异，运行逻辑是：

1. 使用loadDB加载（含有表头）的数据文件，输出的数据格式为字典，表头被舍弃
2. 使用compareData比较两个文件的差异，并输出结果，输出的错误类型（ErrorType）有三种：
	a)but the values are different：同一key在两个文件中的值有差异
	b)is not exit in data2：data1中key所在行，未出现在data2中，即data2有缺失行
	c)is not exit in data1：data2中key所在行，未出现在data1中，即data1有缺失行

3. 若输出'Congratulations! All key values are exactly the same!'则说明两个文件完全一致。
"""

def loadDB(filename):	#load data files
    columnHeading = []
    rowData = {}   
    with open(filename) as f:
        columnHeading = f.readline().strip().split(',')
        for line in f:
            temp = line.strip().split(',')
            rowData[temp[0]] = temp[1:]
        return rowData

def compareData(data1, data2):
	'''compare oldData and newData, return compare results;
	both data type should be dict'''

	#add column heading
	compareResult = ['Key Number'+','+'Data Source'+','+'Error Type']	

	for key in data1:
		if key in data2:
			#for the same key, if value equal to each other, continue
			if data1[key] == data2[key]:	
				continue
			else:
				#for the same key, if value doesn't equal to each other, add error notes to the compareResult		
				compareResult.append((key+','+'in both files'+','+'but the values are different'))
		else:
			#if key isn't exist in data2, add error notes to the compareResult		
			compareResult.append((key+','+'in data1'+','+'is not exit in data2'))

	#if key isn't exist in data1, add error notes to the compareResult
	for key in data2:		
		if key not in data1:
			compareResult.append((key+','+'in data2'+','+'is not exit in data1'))

	#if all key values are exactly tha same, print "Congratulations!"
	if len(compareResult)==1:	
		return ['Congratulations! All key values are exactly the same!']
	#if not, print the result
	else:	
		return compareResult

#an example

d1 = {'ID':['Name','Income','startDate','endDate','Country'],
	 '1174':['James',1000,'2016/4/20','2016/5/20','China'],
	 '1175':['Alex',1000,'2016/4/19','2016/5/20','China'],
	 '1176':['Forrest',1000,'2016/4/20','2016/5/20','USA']}

d2 = {'ID':['Name','Income','startDate','endDate','Country'],
	 '1174':['James',1000,'2016/4/20','2016/5/20','China'],
	 '1175':['Alex',1200,'2016/4/19','2016/5/20','China'],
	 '1177':['Joanna',4000,'2016/4/20','2016/5/20','USA']}

testResult = compareData(d1,d2)
for item in testResult:
	print(item)