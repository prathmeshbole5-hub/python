

countries = ["indian","united states","australia","ireland","srilanka","iceland","cuba","iran","poland"]

# count all the countries starting with the letter 'i'

count = 0
for country in countries:
    if country[0] == 'i':
        count = count + 1

print(count)

# Second method using startswith()

counter = 0
output = []

for country in countries:
    if country.startswith('i'):   # <-- fixed here
        counter = counter + 1
        output.append(country)

print("Count:", counter)
print("Countries:", output)