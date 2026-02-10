words = input("Input: ")
vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
result = ""

for w in words:
    if w not in vowels:
        result += w

print("Output:", result)
