# Name Isam Zia Roll no: TRN-2026-00346 
 
correct_pin = "4321"
attempts = 3

while attempts > 0:
    entered_pin = input("Enter ATM PIN: ")

    if entered_pin == correct_pin:
        print("Welcome")
        break

    attempts -= 1
    print(f"Wrong PIN. Tries left: {attempts}")

    if attempts == 0:
        print("Card blocked")