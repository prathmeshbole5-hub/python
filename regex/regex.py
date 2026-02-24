# regular expression regex
import re 
message ="the current python version is is 3.3.13"

#if python ispresent in message 
"""
print("python" in message)
print("13"in message)
print("14"in message)

print(message.find('3.13'))
print(message.find("python"))
"""

"""
re.search(regex_pattern,string) => returns a match object when there is a match found ,else return n0one
"""

match_obj = re.search('13',message)
print(match_obj)


if re.search('13',message):
    print("found")
else:
    print("not found")