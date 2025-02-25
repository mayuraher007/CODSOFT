#Task4 contactbook

contacts = []

def add_contact(name, phone, email, address):
    contacts.append({'name': name, 'phone': phone, 'email': email, 'address': address})
    print("Contact added successfully!")

def view_contacts():
    print("\nContact List:")
    for contact in contacts:
        print(f"Name: {contact['name']}, Phone: {contact['phone']}")
    print()

def search_contact(search_term):
    print("\nSearch Results:")
    for contact in contacts:
        if search_term.lower() in contact['name'].lower() or search_term in contact['phone']:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
    print()

def update_contact(name, new_phone=None, new_email=None, new_address=None):
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            if new_phone:
                contact['phone'] = new_phone
            if new_email:
                contact['email'] = new_email
            if new_address:
                contact['address'] = new_address
            print("Contact updated successfully!")
            return
    print("Contact not found.")

def delete_contact(name):
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            contacts.remove(contact)
            print("Contact deleted successfully!")
            return
    print("Contact not found.")

def display_menu():
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

while True:
    display_menu()
    choice = input("Enter your choice (1/2/3/4/5/6): ")

    if choice == '1':
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        add_contact(name, phone, email, address)

    elif choice == '2':
        view_contacts()

    elif choice == '3':
        search_term = input("Enter name or phone number to search: ")
        search_contact(search_term)

    elif choice == '4':
        name = input("Enter the name of the contact to update: ")
        new_phone = input("Enter new phone number (leave blank to keep current): ")
        new_email = input("Enter new email (leave blank to keep current): ")
        new_address = input("Enter new address (leave blank to keep current): ")
        update_contact(name, new_phone, new_email, new_address)

    elif choice == '5':
        name = input("Enter the name of the contact to delete: ")
        delete_contact(name)

    elif choice == '6':
        print("Exiting the contact management system. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
