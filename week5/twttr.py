def main():
    words = input("Input: ")
    print("Output:", shorten(words))

def shorten(word):
    vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    result = ""

    for w in word:
        if w not in vowels:
            result += w

    return result

if __name__ == "__main__":
    main()
