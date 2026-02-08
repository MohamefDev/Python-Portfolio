contacts = {}

while True:
    print("\n" + "="*20)
    print("1. Add a contact")
    print("2. View contact")
    print("3. Edit a contact")
    print("4. Exit")
    print("="*20)

    choice = input("Please choose a number from 1-4: ")

    if choice == "1":
        c_id = input("Enter the contact ID: ")
        name = input("Please type a name: ")
        while True:
            phone = input("Please type a phone number: ")
            if phone.isdigit():
                contacts[c_id] = {"name": name, "phone": phone}
                break
            else:
                print("Error: Enter numbers only!")
        print(f"Added: {name}")

    elif choice == "2":
        if not contacts:
            print("Empty!")
        else:
            for c_id in contacts:
                print(f"Name: {contacts[c_id]['name']} | ID: {c_id} | Phone: {contacts[c_id]['phone']}")

    elif choice == "3":
        id_to_edit = input("Enter ID to edit: ")
        if id_to_edit in contacts:
            contacts[id_to_edit]["name"] = input("Enter new name: ")
            while True:
                new_phone = input("Enter new phone: ")
                if new_phone.isdigit():
                    contacts[id_to_edit]["phone"] = new_phone
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
