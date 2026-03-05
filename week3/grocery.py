basket = { }

def main():
    while True:
        try:
            item = input().upper()
            if item in basket:
                basket[item] += 1
            else:
                basket[item] = 1
        except EOFError:
            break
    
    for item in sorted(basket):
        print(basket[item], item)

main()



