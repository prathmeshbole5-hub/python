# w mode = open the file for writing .overwrite a file 
#create a new file if the file doesnat exist 
fh = open("file2.txt",'wt')
fh.write("this is overwriitn using 'w'mode in python\n")
fh.write("have a nice day")
fh.close()



# create directly using w mode 
fh = open("file3.txt",'wt')
fh.write("this is created  using 'w'mode in python\n")
fh.write("have a nice day")
fh.close()
