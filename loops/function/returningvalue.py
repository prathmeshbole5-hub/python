def even_odd(num) :
    if num%2 ==0:
        return"even"
    else:
        return"odd"
    
result =even_odd(9)
print(result)

def arithmatic(num1,num2):
    add=num1+num2
    sub=num1-num2
    mul=num1*num2
    return add ,sub, mul 

val_1 =int(input("enter a number1: "))
val_2=int(input("enter a number2: "))

res1,res2,res3 = arithmatic(val_1,val_2)
print(f"addition of {val_1} and {val_2} is  {res1}")
print(f"addition of {val_1} and {val_2} is  {res2}")
print(f"addition of {val_1} and {val_2} is  {res3}")