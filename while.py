#while condition :
 #stetement
num =1
while num < 5:
    num = num +1 
    print(num) 

correct_password = "2911"
while True:
 user_password =input("enter your pass :  ")
 if user_password == correct_password:
    print("password is correct!")
    break
 else :
    print("wrong password , try again.") 
print("logged in")
