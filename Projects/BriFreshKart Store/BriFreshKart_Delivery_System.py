def record_items():
    items = {}

    items["Item Name"] = input("Enter name of item: ")
    items["Quantity"] = int(input("Enter quantity: "))
    items["Batch Number"] = int(input("Enter your batch number: "))
    items["Expiry Date"] = int(input("Enter expiry year: "))

    print(items)    
    print("Item added successfully!")


def check_expiry(expiry_year):
    if expiry_year < 2025:
        print("Item is expired.")

    elif expiry_year == 2025:
        print("Item expires this year.")

    else:
        print("Item is still valid.")

def main():
         
    while True:
        print("BriFreshKart Delivery")
        print("1. Kumasi")
        print("2. Takoradi")
        print("3. Ho")
        print("4. Bolgatanga")
        print("5. Exit")

        choice = int(input("Select delivery location:"))

        if choice == 1:
            record_items()
            print("Items would be delivered to Kumasi.")

        elif choice == 2:
            record_items()
            print("Items would be delivered to Takoradi.")
            
        elif choice == 3:
            record_items()
            print("Items would be delivered to Ho.")

        elif choice == 4:
            record_items()
            print("Items would be delivered to Bolgatanga.")

        elif choice == 5:
            break

        else:
            print("Please select a valid location.")


if __name__ == "__main__":
    main()

check_expiry(int(input("Please enter the expiry year:")))