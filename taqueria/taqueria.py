def main():
    menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    total = 0.0  # Initial total cost
    while True:
        try:
            # Ask user for the item
            item = input("Item: ").title()
            # Check if the item is in the menu
            if item in menu:
                total += menu[item]  # Add the item's price to the total cost
                print(f"Total: ${total:.2f}")  # Print the total cost
        except EOFError:
            print("\n")
            break  # Break the loop when Control-D (EOF) is pressed

main()
