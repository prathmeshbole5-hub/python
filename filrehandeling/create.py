# x mode=> create the file
fh =open("file2.txt",'xt')

#writing into a file
# write(content)

fh.write("this file is created uint the'x' mode in python.\n")
fh.write("next.line.")
#close the file
fh.close()