text = input()
result = " "

for char in text:
    if char == " ":
        result += "..."
    else:
        result += char

print(result)
