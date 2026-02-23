# range() - built in function used to geerate seqence of integer in a given int 

# for i in range (start stop ,step);
# statement 

for i in range(1 ,10,1):
    print(i)

for i in range(10 ,0,-2):
    print(i)
   
print("happy new year")



profits =[9,11,6,10]
for index in range(len(profits)):
    q = index+1
    print(f"profit for quater{q} is {profits[index]}")