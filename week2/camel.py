camelCase = input("cameCase: ")
result = ""

for c in camelCase:
    if c.isupper():
        result += "_" + c.lower()
    else:
        result += c

print("snake_case:",result)