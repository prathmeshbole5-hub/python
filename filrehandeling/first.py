#opening a file in python
#open(file_name, mode to open)
#modes: r, x, w, a, t, b => 'rt' is the default mode

file_handler = open("file3.txt", "rt")
# Read and print the first 10 characters only
content = file_handler.read(10)
print(content)
print(type(content))
file_handler.close()