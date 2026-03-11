import emoji
message = input("Input: ")
result = emoji.emojize(message, language="alias")
print("Output:", result)


#Algorithm
#1. Import the emoji library
#2. Take a string input from the user
#3. Use the emojize function from the emoji library to 
# convert the input string into emojis
#4. Print the emojized string