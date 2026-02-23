import random

#random() - returns random float value from 0.0 to 1.0

print(random.random()) 

#randint(a,b)=>  returns random in the given value 
print(random.randint(10,15))



nums =[10,2 ,3 ,4 ,5 ,6 ,7]

# choice (sequernce)=> returns a random items 

print(random.choice(nums))


# suffle(sequence)=> returbns the element 
fruits= ["apple","orange","mango"]
print(random.shuffle(fruits))
print(fruits)