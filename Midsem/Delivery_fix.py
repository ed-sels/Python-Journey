import json

def record_items(item_collection):
    items = {}

    item_name = input("Enter name of item: ")
    item_quantity = int(input("Enter quantity: "))
    item_no = int(input("Enter your batch number: "))
    expiry_year = int(input("Enter expiry year: "))

    item_collection[item_name] = item_quantity
    print(f"Item '{item_name}' added successfully.")

def save_items(item_collection):
    """Save the item collection to a file."""
    with open("items.json", "w") as file:
        json.dump(item_collection, file)
    print("Item collection saved successfully.")

def load_items():
    """Load the item collection from a file."""
    try:
        with open("items.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("No item collection found.")
        return {}

def print_items(item_collection):
    """Print all items sorted by year."""
    sorted_items = sorted(item_collection.items(), key=lambda x: x[1])
    for item_name, item_no in sorted_items:
        print(f"{item_name} ({item_no})")

def main():
    item_collection = load_items()
    
    while True:
        print("BriFreshKart Delivery")
        print("Please select your option:")
        print("1. Add an item")
        print("2. Save items")
        print("3. Load and print items")
        print("4. Exit")
        
        choice = int(input("Please select your option:"))

        if choice == 1:
            record_items(item_collection)

        elif choice == 2:
            save_items(item_collection)
            
        elif choice == 3:
            item_collection = load_items
            print_items(item_collection)

        elif choice == 4:
            break

        else:
            print("Please select a valid choice.")

if __name__ == "__main__":
    main()