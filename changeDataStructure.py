# encoding=utf-8


import sys
import numpy as np 

rowData = []

with open('/Users/forrest/Hanhua/HR.csv') as f:
	for line in f:
		temp = line.strip().split(',')
		rowData.append(temp)

t = np.array(rowData)
print(t.shape)

def changeDataStructure(rowData, beigin = 3):
    
    row_length = len(rowData[:,0])  #计算行数
    col_length = len(rowData[0,:])  #计算列数
    
    repeatArea = rowData[1:,:beigin-1]  #固定不变的区域
    valueArea = rowData[1:,beigin-1:]   #数值区域
    valueType = rowData[:1,beigin-1:]   #数值对应的表头名称区域
    
    newRowHead = np.array([])    #新的表头，即第0行    
    newRepeatArea = np.array([])
    newValueType = np.array([])
    newValueArea = np.array([])
    
    repeatTimes = col_length - beigin +1   #需要重复几次
    newRows = (row_length -1 )* repeatTimes

    #新的表头
    oldRowHead = rowData[0,:beigin-1]
    add = np.array(['valueType', 'value'])
    newRowHead = np.hstack([oldRowHead, add])

    #将repeatArea重复N次
    newRepeatArea = np.tile(repeatArea, (repeatTimes, 1))
   
    #将valueType重复n次
    newValueType = valueType.repeat(row_length-1).reshape(-1, 1)

    #将ValueArea进行合并，并转置
    temp = np.array([])
    for i in range(repeatTimes):
        if i==0:
            newValueArea = valueArea[:,i]
        else:
            newValueArea = np.hstack([newValueArea, valueArea[:,i]])
    newValueArea = newValueArea.reshape(newRows, 1)
    
    #生成结果
    tempResult = np.hstack([newRepeatArea, newValueType, newValueArea])
    result = np.vstack([newRowHead, tempResult])  #加上表头
    return result
     
 #   return result

changeResult = changeDataStructure(t,2)
print(changeResult)

r = open('/Users/forrest/Hanhua/resultHR.txt', 'w')
for line in changeResult:
    for item in line:
        r.write(item,)
        r.write(',')
    r.write('\r')
r.close