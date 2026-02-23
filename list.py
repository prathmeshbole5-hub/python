name = "john"
age = 20
percent= 85.5
student =["john",20,85.5]

days_of_week =["MON","tue","wed","thur","fri","sat","sun"]
print(days_of_week[0])
print(student)

# slicing of lists
l1 = [1,2,3,4,5,6,7]
print(l1[1:5:1])

# concatenation of lists 
l4=[1,7,3]
l5= [0,5] 

print(l4+l5)
print(l5*3)

#append()
# add an item in the end of lists
fruits=["apple","mango"]
# syntax : list.append(item)
fruits.append("banana")
print(fruits)

# insert 
# add an element before the specified index 
# syntax list.insert(index,item)

fruits.insert(2,"banana")
print(fruits)

#extend
fruits.extend(["pear","grapes"])
print(fruits)
print(len(fruits))
# remove()
fruits.remove("mango")
print(fruits)

# pop take index to rewmpovw 
fruits.pop(2)
print(fruits) 

d =["MON","tue","wed","thur","fri","sat","sun"]
# reversse

d.reverse()
print(d)
 
nums = [3,4,5,10,7,8] 
nums.sort()
print(nums)

#count()

nummm=[0,0,2,0]
print(nummm.count(0))