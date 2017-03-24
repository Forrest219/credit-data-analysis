# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 15:21:47 2017

@author: admin
"""

import pandas as pd
import time

#加载Excel文件（无需.xlsx后缀），需使用index参数指定索引列，不指定会报错
def load_db(filename, index = None):
    if index == None:
        #若未指定index列，则报错
        return "请指定index列"
    else:
        #打开Excel文件，并用0填充所有空白单元格
        row_data = pd.read_excel(filename+'.xlsx', index_col = index).fillna('0')
    
    #对原数据格式进行“列转行”转换，并重置索引
    reshape_data = row_data.stack().reset_index()
    
    #对转置后的数据列重命名
    final_data = reshape_data.rename(columns = {index:'ID','level_1':'type', 0:'value'})
    
    return final_data
 
    
#对通过load加载的数据进行对比，返回有差异的索引、字段名、原始文件数值和差异值
#暂不支持文本的对比
def compare_data(data1, data2):
    
    # 将两个数据源按指定列，以行的方式合并，在新字段名中以_d1,_d2标识出数据来源
    merge_data = pd.merge(d1, d2, on= ['ID', 'type'], how = 'outer', suffixes = ('_d1','_d2'))

    # 用d1减去d2，并转换为DataFrame格式，新列名为v1-v2
    diff_v1_v2 = pd.DataFrame(merge_data['value_d1'].astype('float')-merge_data['value_d2'].astype('float'), columns =['v1-v2'], index = merge_data.index)

    # 将d1-d2的结果和原始数据进行合并，共用相同索引
    temp_check_result = pd.merge(merge_data, diff_v1_v2, left_index = True, right_index=True)

    # 创建v1-v2列值不等于零的布尔筛选器
    filter_not_zero = temp_check_result['v1-v2']!= 0

    #通过筛选器，输出v1-v2值不为零的行
    check_result =  temp_check_result[filter_not_zero]
    
    #获取对比时间
    compare_time = time.strftime('%Y%m%d',time.localtime(time.time()))
    
    check_result.to_excel('python_result'+'_'+compare_time + '.xlsx', index = False)
    
    print '对比结果已输出！'


d1 = load_db('BI', index = 'ID')
d2 = load_db('customer', index = 'ID')

compare_data(d1, d2)