contacts = {}

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    address = input("Enter address: ")
    contacts[name] = {"Phone": phone, "Email": email, "Address": address}
    print(f"Contact {name} added.")

def view_contacts():
    if not contacts:
        print("No contacts available.")
    else:
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['Phone']}, Email: {info['Email']}, Address: {info['Address']}")

def search_contact():
    name = input("Enter the name to search: ")
    if name in contacts:
        info = contacts[name]
        print(f"Name: {name}, Phone: {info['Phone']}, Email: {info['Email']}, Address: {info['Address']}")
    else:
        print(f"Contact {name} not found.")

def update_contact():
    name = input("Enter the name to update: ")
    if name in contacts:
        phone = input("Enter new phone number: ")
        email = input("Enter new email address: ")
        address = input("Enter new address: ")
        contacts[name] = {"Phone": phone, "Email": email, "Address": address}
        print(f"Contact {name} updated.")
    else:
        print(f"Contact {name} not found.")

def delete_contact():
    name = input("Enter the name to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted.")
    else:
        print(f"Contact {name} not found.")

while True:
    print("\n1. Add Contact\n2. View Contacts\n3. Search Contact\n4. Update Contact\n5. Delete Contact\n6. Exit")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        add_contact()
    elif choice == 2:
        view_contacts()
    elif choice == 3:
        search_contact()
    elif choice == 4:
        update_contact()
    elif choice == 5:
        delete_contact()
    elif choice == 6:
        break
    else:
        print("Invalid choice. Please try again.")
