text = input("Input: ")
new_text = ""

for i in text:
    if i.lower() not in ["a" , "e" , "i" , "o" , "u"]:
        new_text += i

print(new_text)