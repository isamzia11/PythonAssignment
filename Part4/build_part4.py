    # Name Isam Zia Roll no: TRN-2026-00346 

contacts = {
    "Ali": "03001111111",
    "Sara": "03002222222",
    "Ahmed": "03003333333",
    "Zara": "03004444444",
    "Hamza": "03005555555"
}

while True:
    print("\n===== PHONE BOOK =====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Show All")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone
        print("Contact added successfully!")

    elif choice == "2":
        name = input("Enter name to search: ")
        phone = contacts.get(name)

        if phone is not None:
            print(f"{name}: {phone}")
        else:
            print("Not found")

    elif choice == "3":
        name = input("Enter name to delete: ")

        if name in contacts:
            del contacts[name]
            print("Contact deleted")
        else:
            print("Not found")

    elif choice == "4":
        for name, phone in contacts.items():
            print(f"{name}: {phone}")

    elif choice == "5":
        print("Exiting Phone Book")
        break

    else:
        print("Invalid choice")