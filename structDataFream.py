# encoding=utf-8

rowData = []
col = []
with open('dataframe.csv') as f:
	for line in f:
		temp = line.strip().split(',')
		rowData.append(temp)

#print(rowData)

def structDataFrame(rowData, n=3):
	'''n represastns '''

	result = []

	rowLength = len(rowData[0])	#列数
	colLength = len(rowData)	#行数

	repeatArea = []

	for i in range(1,4):
		for j in range(2):
			temp.append(rowData[i][j])
		repeatArea.append(temp)

	print(repeatArea)

structDataFrame(rowData)








	