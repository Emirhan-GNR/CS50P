case = input("camelCase: ")
new = ""

for i in case:
    if i.isupper():
        new += "_" + i.lower()
    else:
        new += i

print(new)