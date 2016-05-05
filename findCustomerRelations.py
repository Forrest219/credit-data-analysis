#  coding=utf-8
#
#  文件名:  findCustomerRelations.py
#  功能:    找到客户之间的关联关系
#  作者：Forrest219

import codecs

# 加载原文件

def loadCustomerDB(filename):
	columnHeading = []
	customerData = []
	try:
		with open(filename) as f:
			columnHeading = f.readline().strip().split(',')
			for line in f:
				temp = line.strip().split(',')
				customerData.append([temp[0], temp[1]])
			return customerData
	except IOError as ioerror:
		print('File error:' + str(ioerror))
		return None

#--Test--
test = loadCustomerDB("findCustomerRelations.csv")
print(test)

class findCustomerRelations:

	def __init__(self, data):
		"初始化 findCustomerRelations; 如果data是列表， findCustomerRelations将直接完成初始化。如果是其他类型的数据，需要先转换为列表"

		#如果data的类型为“列表”，则直接使用data
		if type(data).__name__ == 'list':
			self.data = data

#	def computeRelatedCustomers(self, customerName):
#		relatedCustomerList = []
#		for customer in self.data:
#			if customer not

#	def findRelatedCustomers(self, customerName):
#		"给出指定客户的关联客户"
#		if customerName in self.data:
#			print(customerName)
#		else:
#			print('ll')

def computeCustomerRelations(customerData):

	customerRelations = {}

	fild1 = []
	fild2 = []
	temp = []

	#将customerRelations分成两个部分
	for item in customerData:	
		if len(set(item)) > 1:	#如果对列表去重后客户数量大于1，
			fild1.append(item)
		else:
			for newItem in item:
				temp.append(newItem)
				fild2 = list(set(temp))
	return fild1
	

#从customerRelationsData中找到customerName的关联客户，输出关联客户、非关联客户集
def findRelatedCustomers(customerName, customerRelationsData):

	relatedCustomer = []
	newCustomerRelationsData = []
	alreadyUsed = []	

	for item in customerRelationsData:	#如果customerName在item中，则从原始数据中删除该元素
		if customerName in item:
			temp = relatedCustomer + item
			relatedCustomer = list(set(temp))
		else:
			newCustomerRelationsData.append(item)	#保存非关联客户集
		
		alreadyUsed.append(customerName)

	return [relatedCustomer, newCustomerRelationsData]

#--TDD---
t = findRelatedCustomers('a', test)
print(t)

def findRelatedCustomers2(customerList, customerRelationsData):

	relatedCustomer = customerList
	newCustomerRelationsData = []
	alreadyUsed = []	
	customerRelationsData = customerRelationsData

	for eachCustomer in customerList:
		for eachItem in customerRelationsData:
			if eachCustomer in eachItem:
				temp = relatedCustomer + eachItem
				relatedCustomer = list(set(temp))
			else:
				customerRelationsData.append(eachItem)

	return [relatedCustomer, customerRelationsData]

t3 = t[1]
#print(t[0], t[1])

t4 = findRelatedCustomers2(t[0], t[1])
print(t4)


#对客户关系列表中包含的元素进行去重，得到客户列表
#customerRelationsData必须是二维嵌套的列表
def getCustomerlist(customerRelationsData):
	customer = []
	temp = []

	for item in customerRelationsData:
		for newItem in item:
			temp.append(newItem)
	result = list(set(temp))
	return result

#==TTD
#customer1 = getCustomerlist(test)
#print(customer1)

#t = [['a', 'b'], ['a', 'c'], ['c', 'c'], ['d', 'd'], ['e', 'e'], ['f', 'f'], ['g', 'f']]


#print(findRelatedCustomers(['a', 'b'], t2))