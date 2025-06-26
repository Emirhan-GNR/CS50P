amount_due = 50
print("Amount Due: " + str(amount_due))

while True:
    coin =input("Insert Coin: ")
    if coin in ["5","10","25"]:
        amount_due -= int(coin)
        if amount_due > 0:
            print("Amount Due: " + str(amount_due))
        elif amount_due <= 0:
            owed = (-amount_due)
            print("Change Owed: " + str(owed))
            break