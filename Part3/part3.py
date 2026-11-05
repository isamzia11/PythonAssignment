
# Name Isam Zia Roll no: TRN-2026-00346

while True:

    print("\n===== MAIN MENU =====")
    print("1. Say Hello")
    print("2. Print Numbers 1 to 10")
    print("3. Multiplication Table")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Hello! Welcome to Python.")

    elif choice == "2":
        for number in range(1, 11):
            print(number)

    elif choice == "3":
        try:
            num = int(input("Enter a number: "))

            for i in range(1, 11):
                print(f"{num} x {i} = {num * i}")

        except ValueError:
            print("Please enter a valid whole number.")

    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.")
