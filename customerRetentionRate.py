# encode = utf-8
import datetime
from itertools import groupby
import csv

def strDate2Date(str_date):
    date = datetime.datetime.strptime(str_date, '%Y/%m/%d')
    return date

def dateDelta(date1, date2):
    dateDelta = (date2-date1).days
    return dateDelta    

def printBusInfo(busInfo_lsit):
    for item in busInfo_lsit:
        print(item.busID, item.customerID, item.startDate, item.endDate, item.dateDelta)

class busInfo:
    def __init__(self, busID, customerID, startDate, endDate, dateDelta = None):
        self.busID = busID
        self.customerID = customerID
        self.startDate = startDate
        self.endDate = endDate
        self.dateDelta = None

#计算时间间隔
def calculateDays(busInfo_list, endDate):
    """给定日期，计算它与下一次续贷发生日期间的时间间隔；
        busInfo+_list需是同一个customerID名下的所有业务
        endDate是给定的日期"""
    result = []
    startDate_List = []   #存储续做业务的发生日期，以便找出最小日期
    
    for item in busInfo_list:
        if 'stay' in result:
            break #如果当项目结束时，有其他在保在贷项目时，结束迭代
        elif item.startDate < endDate < item.endDate:
            result.append('stay')  #stay表示解保时有其它在保、在贷项目
            break
        elif item.startDate >= endDate:
            startDate_List.append(item.startDate)
        else:
            continue 
    
    if 'stay' in result:    #如果当项目结束时，有其他在保在贷项目时，返回“stay”
        return 'stay' 
    elif len(startDate_List) == 0:
        return 'wu xu zuo'
    else:
        latest_startDate = min(startDate_List)
        result = dateDelta(endDate, latest_startDate) 
        return result
        
#加载数据
heading = []
rowData = []

with open('C:/Users/X240/Documents/GitHub/data/busInfo v20160616.csv') as data:
    heading = data.readline()
    for each_line in data:
        temp = each_line.strip().split(',')
        rowData.append(busInfo(temp[0], temp[1], strDate2Date(temp[2]), strDate2Date(temp[3])))

#测试calculateDays函数
#for item in rowData:
 #   item.dateDelta = calculateDays(rowData,item.endDate)
 #   print(item)

#对加载的数据进行排序、分组，生成字典型数据类型，其中customerID是Key
rowData.sort(key= lambda x: x.customerID)   #使用groupby前必须先排序
groupby_rowData = groupby(rowData, lambda x: x.customerID) #使用groupby对rowData进行分组
data = dict([(key,list(group)) for key,group in groupby_rowData]) #生成字典型数据结构    

#print(data)
#printBusInfo(rowData)

result = [] #存储运算结果
for key in data:
    for item in data[key]:
        item.dateDelta = calculateDays(data[key], item.endDate)
        result.append(item)
 
#printBusInfo(result)    #打印运算结果
3
#输出运算结果

with open('D:/HanHua OM/om10 to Python/xuzuo_result4.csv', 'w') as r:
#r = open('D:/HanHua OM/om10 to Python/xuzuo_result4.csv', 'w')
    for item in result:
        temp = []
        temp.extend([item.busID, item.customerID, item.startDate, item.endDate, item.dateDelta])
#    for nitem in temp:
        r.write(str(temp))
        r.write('\r')
r.close
print('Finshed!')