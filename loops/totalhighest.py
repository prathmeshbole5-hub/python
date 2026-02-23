scores =[2,45,67,4,9,10,98,79,89]
print(len(scores))

total = 0
 
for score in scores:
    total= total+score

print(f"total scored meaure i{total}")


highest = scores [0]

for score in scores:
    if highest < score:
        highest =score

print(f"the highest value is {highest}")