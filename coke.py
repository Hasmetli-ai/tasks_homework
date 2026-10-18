import time
amount=50
print("Welcome to the coke machine!!")
time.sleep(2)
print(f"amount of coke is {amount}")
time.sleep(2)
print("Please enter 5,10 or 25 coins")
time.sleep(2)
while amount>0:
    print(f"Amount due: {amount}")
    inserted_coin=int(input("Insert coin: "))
    if inserted_coin!=25 and inserted_coin!=10 and inserted_coin!=5:
        print("Please enter valid coin!!!!!"
               "fx:25,10 or 5")
        continue
    amount-=inserted_coin
change_owed=-amount
print(f"Amount due: 0")
print(f"Change owed: {change_owed}")