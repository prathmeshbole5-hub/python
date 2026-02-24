try:
    with open("file2.txt","rt") as fh:
        data =fh.read
        fh.close()

except FileNotFoundError as file_err:
    print("file that you are trying to open doenot exost")
    print(file_err)

else:
    print(data)
finally:
    print("finally block")