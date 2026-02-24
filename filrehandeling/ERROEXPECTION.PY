
try :
    num1=int(input("enter the number:   "))
    num2 =int(input("enter the number r2: "))
    result =num1/num2
    print(result)
except ZeroDivisionError:
    print("the the denomitior is zero ")
except ValueError:
    print("input sholud only be digit")

             

