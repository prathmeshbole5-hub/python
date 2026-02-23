#range()-BUILT IN FUCNTION USED  TO GENERATE SEQUENCE IN THE GIVEN OINT 
 #RANGE(START ,STOP ,STEP) 
# (range(start,stop))=> 1 by default 
# range(stop)=> o to stop-1 with a step of 1 ,satrt =0 by defaut


for i in range(2,20,2) : 
 print(i)
 

groceries = ['salt','milk','sugar']
for item in groceries :
  print(item )

scores =[2,45,102,3,4,13 ,45 ,69,78,100,101]
total = 0
for score in scores :
  total =total + score 
  print(f"total run scored is {total}")

for num in range(10):
  if num % 3 == 0:
    continue 
  print(num)
  

for num in range(1,10):
  if num % 3 == 0:
    break
  
  print(num)
  