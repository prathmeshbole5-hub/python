def greeting_someone(name):
    print(f"hello {name} ,good morning!")
    print("its a beautiful day")

#calling a function
greeting_someone("prathmesh")

def even_odd(number):
    if number%2==0:
        print("the number is even")
    else:
        print("odd")

even_odd(10)
even_odd(55)

                 
def add(num1,num2):
    result =num1+num2
    print(f"result: {result}")

add(10,3)
add(9,-4)