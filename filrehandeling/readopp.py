#opening a file in python
#open(file_name,mode_to_open)

file_handler=open("file1.txt",'rt')

# read operation 
# read() => read the content of file as stre

content =file_handler.read(10)
#read line readline()
content1 =file_handler.readline()
#file_handler.close()

# closina a file => close()
file_handler.close()
print(content)
print(content1)
print(type(content))
#print(file_handler)