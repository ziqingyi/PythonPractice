
old_file_name = input("please input file's name: ")

f_read = open(old_file_name, "r")

#new_file_name = old_file_name+"copy.py"

position = old_file_name.rfind(".")
new_file_name = old_file_name[0:position]+"copy"+old_file_name[position:]

f_write = open(new_file_name,"w")

content = f_read.read()
f_write.write(content)




f_read.close()
f_write.close()











