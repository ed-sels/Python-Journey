# Initialize an empty dictionary to store contacts
contacts = {}

def add_contact():
    name = input("Enter name: ")
    phone_number = input("Enter phone number: ")
    contacts[name] = phone_number
    print("Contact added successfully!")

def search_contact():
    name = input("Enter name to search: ")
    if name in contacts:
        print("Phone Number:", contacts[name])
    else:
        print("Contact not found!")

def update_contact():
    name = input("Enter name to update: ")
    if name in contacts:
        phone_number = input("Enter new phone number: ")
        contacts[name] = phone_number
        print("Contact updated successfully!")
    else:
        print("Contact not found!")

def delete_contact():
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")

def display_contacts():
    if contacts:
        print("\nPhonebook:")
        for name, phone_number in contacts.items():
            print(f"{name}: {phone_number}")
    else:
        print("Phonebook is empty!")

def main():
    while True:
        print("\nPhonebook Menu:")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Display Contacts")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            search_contact()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            display_contacts()
        elif choice == "6":
            print("\nFinal Phonebook:")
            display_contacts()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()