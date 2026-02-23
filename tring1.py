s1 = "hello world"
print(s1)
print(len(s1))
print("first char",s1[0])
print("last char ",s1[-1]) 
"""
syntax of indexing : string[index]
syntax of slicing :string[start:end:step] 
"""
print(s1[2:7:1])

s2= "raj rane"
print(s2)
print(s2[3:6:1])

name= "john"
age = 20
language ="python"
hours=3 
print(f"{name} is {age} years old he studied {language}{hours} hours a day,")

a=20
b=50
print(f"{name} scored {a+b} years old he studied {language}{hours} hours a day,")
print(s1 *  5)
# membership operator 
#in
s4="python is fun"
print("python" in s4)
print("i" in s1)

print("python" not in s4)
print("i" not in s1)
# strip() remove space from string
# replace 
s5 = "we are learning python"
print(s5)
print(s5.replace("python","java" ))
print(s5.count(s5))