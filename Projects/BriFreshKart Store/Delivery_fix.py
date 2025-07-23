import json

def record_items(item_collection):
    item_name = input("Enter name of item: ")
    item_quantity = int(input("Enter quantity: "))
    item_no = int(input("Enter your batch number: "))
    expiry_year = int(input("Enter expiry year: "))

    # Store all item details
    item_collection[item_name] = {
        "quantity": item_quantity,
        "batch_no": item_no,
        "expiry_year": expiry_year
    }

    print(f"Item '{item_name}' added successfully.")

def save_items(item_collection):
    """Save the item collection to a file."""
    with open("items.json", "w") as file:
        json.dump(item_collection, file, indent=4)
    print("Item collection saved successfully.")

def load_items():
    """Load the item collection from a file with error handling."""
    try:
        with open("items.json", "r") as file:
            content = file.read().strip()
            if not content:
                print("Item file is empty. Starting with an empty collection.")
                return {}
            return json.loads(content)
    except FileNotFoundError:
        print("No item collection found. Starting fresh.")
        return {}
    except json.JSONDecodeError:
        print("Item file is corrupted or contains invalid JSON. Starting with an empty collection.")
        return {}

def print_items(item_collection):
    """Print all items sorted by expiry year."""
    if not item_collection:
        print("No items to display.")
        return

    # Sort by expiry year
    sorted_items = sorted(item_collection.items(), key=lambda x: x[1]["expiry_year"])
    
    for item_name, details in sorted_items:
        print(f"{item_name}: Quantity = {details['quantity']}, "
              f"Batch No = {details['batch_no']}, Expiry Year = {details['expiry_year']}")

def main():
    item_collection = load_items()
    
    while True:
        print("\nBriFreshKart Delivery")
        print("Please select your option:")
        print("1. Add an item")
        print("2. Save items")
        print("3. Load and print items")
        print("4. Exit")
        
        choice = input("Please select your option: ")

        if choice == "1":
            record_items(item_collection)

        elif choice == "2":
            save_items(item_collection)

        elif choice == "3":
            item_collection = load_items()
            print_items(item_collection)

        elif choice == "4":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Please select a valid choice.")

if __name__ == "__main__":
    main()
