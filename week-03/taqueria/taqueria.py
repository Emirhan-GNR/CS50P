menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total_price = 0

try:
    while True:
        selection = input("Item: ")
        price = menu.get(selection.title())
        if price:
            total_price += price
            print(f"Total: ${total_price:.2f}")
except EOFError:
    print()