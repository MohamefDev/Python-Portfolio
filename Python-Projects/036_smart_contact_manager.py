contact = {}

while True:
    print("\n" + "="*20)
    print("1. Add a contact")
    print("2. View contact")
    print("3. Edit a contact")
    print("4. Exit")
    print("="*20)
    
    choice = input("Please choose a number from 1-4: ")

    if choice == "1":
        contact["ID"] = input("Enter the contact ID: ")
        contact["name"] = input("Please type a name: ")
        
        while True:
            phone = input("Please type a phone number: ")
            if phone.isdigit():
                contact["phone"] = phone
                break
            else:
                print("Error: Enter numbers only!")
        print(f"Added: {contact['name']}")

    elif choice == "2":
        if not contact:
            print("Empty!")
        else:
            print(f"Name: {contact['name']} | ID: {contact['ID']} | Phone: {contact['phone']}")

    elif choice == "3":
        id_to_edit = input("Enter ID to edit: ")
        if id_to_edit == contact.get("ID"):
            contact["name"] = input("Enter new name: ")
            while True:
                new_phone = input("Enter new phone: ")
                if new_phone.isdigit():
                    contact["phone"] = new_phone
                    break
                else:
                    print("Numbers only!")
            print("Updated!")
        else:
            print("ID not found!")

    elif choice == "4":
        break
    else:
        print("Invalid choice!")
