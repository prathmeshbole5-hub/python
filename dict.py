# comma spereted key value pairs enclosed within{}
# {key :value ,key2:value2 ,....}


groceries = {'milk' : 60 ,'biscuit':20, 'rice' : 90,'bread':30} 
#dicT ARE MUTABLE 
print(groceries['milk'])
groceries['milk']= 65 
print(groceries)
groceries['eggs']=10 # adds ney key value pair to the dictionary groceries 
print(groceries)

marks={"maths":80.5,"eng":76.0 }
# get 
print(marks.get("chem",40.0))

#memberhip operator => in not in
print('name'in marks)

sem1= {"eng":40,"maths":50,"phy":80}
sem2= {'chem':81.5,'bio':90.5}
sem1.update(sem2)
print(sem1)
groceries1 = {'milk' : 60 ,'biscuit':20, 'rice' : 90,'bread':30} 
#pop ()
sem1.pop('eng')
print(sem1)

d11={[]}