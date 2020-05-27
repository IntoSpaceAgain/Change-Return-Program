"""Develop a program that has the user enter the cost of an item and then the amount the user paid for the item. Your program should figure out the change and the number of coins needed for the change.
"""
coins_dict = {"£2": 2.00, "£1": 1.00, "50p": 0.50, "20p": 0.20,
              "10p": 0.10, "5p": 0.05, "2p": 0.02, "1p": 0.01}

def valid_input(msg):
    while True:
        try:
            user_input = float(input(msg))
            return user_input
        except ValueError:
            print("Invalid input. Please make sure to use only numbers.")

# User to input the item_cost and the amount_paid
item_cost = valid_input("How much did the item cost? £")
amount_paid = valid_input("How much money have you paid? £")
if amount_paid < item_cost:
    print(f"Please pay an extra £{item_cost - amount_paid}")
else:
    # Calculate change: amount_paid - item_cost
    change = amount_paid - item_cost
    print(f"Change: {change}")
    # Number of each coin to return
    for coin_name, coin_value in coins_dict.items():
        count = int(change / coin_value)
        change = round(change % coin_value, 2)
        print(f"Number of {coin_name} coins to return: {count}")