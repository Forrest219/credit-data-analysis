#  coding=utf-8
#
#  文件名:  findCustomerRelations.py
#  功能:    找到客户之间的关联关系
#  作者：Forrest219

from sets import Set


def loadCustomerDB(filename, path = ''):
	"""load the business_info data"""
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
#test = loadCustomerDB("findCustomerRelations.csv")
#print(test)

businessInfo = [['a','b'], ['a','c'], ['c','c'], ['d','e'], ['e','e'], ['f','f'], ['g','f']]
print(businessInfo)

setBusinessInfo = map( lambda item : Set(item), businessInfo)
print(setBusinessInfo)

def calculate(list):	
	result = [] # put the final  set here	
	
	def merge(list):
		if len(list) == 0:
			return
		for index in range(1,len(list)):				
			if list[0].intersection(list[index]):
				list[index] = list[index].union(list[0]) # merge the two sets if has intersection
				return merge(list[1:])  # and stop loop immediatelly
		result.append(list[0]) # list[0] is the final set, because it has no intersection with other sets
		return merge(list[1:]) # start the new loop to merge 
	 
	merge(list)		
	return result

result = calculate(setBusinessInfo)
print(result)