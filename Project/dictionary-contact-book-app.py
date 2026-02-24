
main_menu = """Contact Book Menu:
1. Add Contact
2. View Contact
3. Edit Contact
4. Delete Contact
5. List All Contacts
6. Exit
"""
print(main_menu)

def display_menu():
    print(main_menu)

def add_contact(contact_book):
    name = input()
    phone = input()
    email = input()
    address = input()

    if name in contact_book:
        print("Contact already exists!")
    else:
        contact_bk[name] = {
        "phone": phone,
        "email": email,
        "address": address
        }
        print("Contact added successfully!")

contact_bk = eval(input())
# add_contact(contact_bk)


def view_contact(contact_book):
    name = input()
    if name in contact_book:
        details = contact_book[name]
        print(f"Name: {name}")
        print(f"Phone: {details['phone']}")
        print(f"Email: {details['email']}")
        print(f"Address: {details['address']}")
    elif name not in contact_book:
        print("Contact not found!")

def edit_contact(contact_book):
    name = input()
    if name in contact_book:
        new_phone = input()
        if new_phone:
            contact_book[name]["phone"] = new_phone
        new_email = input()
        if new_email:
            contact_book[name]["email"] = new_email

            
        new_address = input()
        if new_address:
            contact_book[name]["address"] = new_address


        # contact_book[name]["phone"] = input()
        # contact_book[name]["email"] = input()
        print("Contact updated successfully!")
        # contact_book[name]["address"] = input()
    elif name not in contact_book:
        print("Contact not found!")

def delete_contact(contact_book):
    name = input()
    if name in contact_book:
        contact_book.pop(name)
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")

def list_all_contacts(contact_book):
    if contact_book:
        # details = contact_book[name]
        for name in contact_book:
            details = contact_book[name]
            print(f"Name: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}\n")
    else:
        print("No contacts available.")

list_all_contacts(contact_bk)