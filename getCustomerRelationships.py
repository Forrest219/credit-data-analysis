# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 10:04:30 2016

@author: Forrest

本脚本通过为“关联客户”设置相同的customerID，帮助分析人员识别关联客户。

"""
from sets import Set
import sys   
sys.setrecursionlimit(10000000) #reset maximum recursion depth 
        
def loadDB(filename,heading=True):
    '''load data files; if heading=True, delect the first line'''
    rowData = []
    with open(filename) as f:
        for each_line in f:
            rowData.append(each_line.strip().split(','))
        
        if heading == True: #if heading is in the first line, delect it
            rowData.pop(0)
            
        return map(lambda item: Set(item), rowData)

def calculate(data_list):	
    result = [] # put the final set here 

#    data_set = map(lambda item: Set(item), data_list)
    def merge(list):
		if len(list) == 0:
			return
		for index in range(1,len(list)):				
			if list[0].intersection(list[index]):
				list[index] = list[index].union(list[0]) # merge the two sets if has intersection
				return merge(list[1:])  # and stop loop immediatelly
		result.append(list[0]) # list[0] is the final set, because it has no intersection with other sets
		return merge(list[1:]) # start the new loop to merge 

    merge(data_list)	
    return result
    
def getCustomerList(data_set):
    '''data_set is a set type data'''
    result = []
    for item in data_set:
        result.extend(list(item))
    
    return Set(result) 

def creatID(list_in_list):
    result = []
    length = len(list_in_list)
    for i in range(length):
        for customer in list_in_list[i]:
            result.append([customer, i])
    return result 

def getResult(data):
    result = []
    
    # seperate data into two parts    
    data_for_calculate = []
    data_the_rest = []
    for item in data:
        if len(item)>1:
            data_for_calculate.append(item)
        else:
            data_the_rest.append(item)
    
    #calculate data_for_calculate
    calculate_result = calculate(data_for_calculate)
    customerList_for_calculate = getCustomerList(data_for_calculate)
    customerID_for_calculate = creatID(calculate_result)
    
    allCustomer = getCustomerList(data) #get all customer ID's lsit 
 
    i = len(calculate_result)
    result = customerID_for_calculate
    for customer in customerList_for_calculate:
        allCustomer.remove(customer)

    for customer in allCustomer:
        result.append([customer,i])
        i+=1
    
    return result

def write(data):
    with open('D:/HanHua OM/om10 to Python/customerRelationships_20160620.csv', 'w') as f:
        for each_line in data:
            for item in each_line:
                f.write(str(item))
                f.write(',')
            f.write('\n')
            
# Run the scripts!
            
#first:load the data
data =loadDB('C:/Users/X240/Documents/GitHub/data/realtedCustomer.csv', heading = True)

#second:get the result
result = getResult(data)
print(len(result))
#In the end:write the result into a csv file
write(result)
