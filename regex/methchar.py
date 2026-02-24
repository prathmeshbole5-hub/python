import re

message = "the current python versionis 3.13.  other previous version are 3.12,3.11,3.10"

match_object =re.search("[0-9][0-9]",message)
print(match_object)

match_object = re.search("[0-9][0-9][0-9]","house number: 251/A")
print(match_object)