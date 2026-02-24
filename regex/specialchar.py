import re
s1= "python i easy programming language"

#[a-z],[A-z]

pat =r"old\new"
print(pat)

#match_obj =re.search()

pat =r"[a-z][a-z]"
match_obj =re.search(pat,s1)
print(match_obj)
