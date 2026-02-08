contacts = {}

while True:
    print("\n" + "="*20)
    print("1. Add a contact")
    print("2. View all contacts")
    print("3. Edit a contact")
    print("4. Delete a contact")
    print("5. Exit")
    print("="*20)

    choice = input("Please choose a number from 1-5: ")

    if choice == "1":
        c_id = input("Enter the contact ID: ")
        name = input("Please type a name: ")
        while True:
            phone = input("Please type a phone number: ")
            if phone.isdigit():
                # تخزين كل جهة اتصال في 'مفتاح' خاص بها بناءً على ID
                contacts[c_id] = {"name": name, "phone": phone}
                break
            else:
                print("Error: Enter numbers only!")
        print(f"Added: {name}")

    elif choice == "2":
        if not contacts:
            print("Empty!")
        else:
            # عرض جميع جهات الاتصال المخزنة باستخدام حلقة تكرار
            for c_id in contacts:
                print(f"ID: {c_id} | Name: {contacts[c_id]['name']} | Phone: {contacts[c_id]['phone']}")

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
        id_to_del = input("Enter ID to delete: ")
        if id_to_del in contacts:
            del contacts[id_to_del]
            print("Deleted successfully!")
        else:
            print("ID not found!")

    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice!")
