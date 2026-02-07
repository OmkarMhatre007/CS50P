amount_due = 50
insert_coin = ""

while amount_due > 0:
    print("Amount Due:",amount_due)
    insert_coin = int(input("Insert coin: "))
    if insert_coin == 25 or insert_coin == 10 or insert_coin == 5:
        amount_due = amount_due - insert_coin
    
print("Change Owed:",abs(amount_due))

