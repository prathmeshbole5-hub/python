"""we have the following dictionaory containg details 

user ={ 
"user_name":"my_user",
"pasword":"test@123"
"email":"muser@gamil.com"
"address":"abc road,11111",
"country":"australia"
}

delete the sensitive information from the dictionaruy present in the list sensetive_info=["pasword","address"]
"""
user = { 
    "user_name": "my_user",
    "password": "test@123",
    "email": "muser@gamil.com",
    "address": "abc road,11111",
    "country": "australia"
}

sensitive_info = ["password", "address"]

for i in sensitive_info:
    print(f"key: {i}, value: {user[i]}")
    if i in user:
         print(f"key: {i}, value: {user[i]}")
    user.pop(i)
else:
    print(f"{i} not present")

print(user)