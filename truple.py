#truple (item1, items 2)
t1 = ("python",10,1.5, True ,[1,2,4],(10,20))
print(t1)
print(len(t1))

#accesibg the index of truple 

print(t1[0])






"""
concatenation ,repetation ,memebership 
count,index 
min max sum 
"""
a = (1,2,3,4,5,)
b= ("gyan","nobita",2,3)
c = a+b
print(c)

# rep *
d = a *4 
print(d)

# membership in not in , truples and tring  are immutable 
print(2 in a)
print("suniya"not in b)
# count 
print(a.count(1))
# truple.index(element)
print(a.index(2))

h = (23,34,56,78,90,87,75)
#min(tuple)
#max(tuple)
#sum(tuple)
print(f"smallest number :{min(h)}")
print(f"hihest num  :{max(h)}")
print(f" total: {sum(h)}") 

#mutiblituly and inmuteblity 

l1= ["mango","orange","aple"]
print(id(l1))
l1[-1] ='apple'
print(l1)
print(id(l1))
 