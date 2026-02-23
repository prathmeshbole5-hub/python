import random
print("welcome to the game of rolling the die ")
while True:
    choice=input("press'enter' to roll the dice or'q'to quit.")
    if choice =='q':
        print("thanks for playing the game ,bye!")
        break
    elif choice =='':
        number =random.randint(1,6)
        print(f"your number is {number}")
    else:
        print("invalid input!!")    


        
