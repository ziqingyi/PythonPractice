import os


for file in os.listdir('.'):

	if file[-2: ] == 'py':
		continue

	if len(file) > 12:
		continue

	list=file.split(".")

	name = list[0]
	#print(list[0])
	#print(name[1])
	newname = name[4:8]+name[2:4]+name[0:2]+".pdf"

	print ("file name is: %s " % (file))
	print("new name is: %s"%newname)

	os.rename(file,newname)



#print ("--------- " )






















