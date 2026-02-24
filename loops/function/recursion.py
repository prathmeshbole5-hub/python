def fact(num):
 if num ==1:
  return 1
 else:
  factorial =num * fact(num-1)
  return factorial
print(fact(4))
