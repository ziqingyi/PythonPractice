import os
import xlrd
from pyexcel_xls import get_data

fileaddress = '‪D:\xxxxx\name.xlsx'

data=xlrd.open_workbook('name.xlsx')
	
table=data.sheet_by_name(u'Sheet2')
	
nrows=table.nrows
ncols=table.ncols
print(nrows)

for rowNum in range(0, nrows-1):  
	cellvalue= table.cell(rowNum,0).value
	print (cellvalue)

rowNum = 0
	
for file in os.listdir('.'):

	if file[-2: ] == 'py':
		continue
	if file[-4: ] == 'xlsx':
		continue
	if file[-3: ] == 'exe':
		continue
	if file[-3: ] == 'rtf':
		continue

	list=file.split(".")

	name = list[0]
	#print(list[0])
	#print(name[1])

	print ("file name is: %s " % (file))
	
	newname= table.cell(rowNum,0).value
	newname=newname +".mp4"
	print ("the name should be: %s" %newname)

	os.rename(file, newname)

	print("----------------------------------------")
	rowNum= rowNum + 1

	
	#newname = name[4:8]+name[2:4]+name[0:2]+".mp4"

























