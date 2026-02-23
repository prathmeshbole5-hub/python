# hallow copy 
import copy

l1 =[1,2.5,[10,20,30],'python']

l2 = copy.copy(l1)
print(l2)
print(id(l1))
print(id(l2))
l1[0]= 5
l1[2][0]= 50
print(f"l1->{l1}",id(l1))
print(f"l2->{l2}",id(l2))