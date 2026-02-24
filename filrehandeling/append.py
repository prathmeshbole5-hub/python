#'a' mode=> append mode

# if file doe not exist 'a mode creates the file 
fh=open("file2.txt",'at')
fh.write("\nthis content has been written using 'a' mode.\n ")
fh.write("good bye")
fh.close()