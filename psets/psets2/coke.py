amount_due=50
while amount_due>0:
    print("Amount Due:", amount_due)
    coin=int(input("Insert coin: "))
    if coin in [5,10,25]:
        amount_due-=coin

print("Change Owed:",abs(amount_due))
