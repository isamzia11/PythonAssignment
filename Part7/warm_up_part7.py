# Name Isam Zia Roll no: TRN-2026-00346 


def safe_division():
    while True:
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            result = a / b

            print(f"Result: {result:.2f}")
            break

        except ValueError:
            print("Error: Please enter numbers only.")

        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")


safe_division()
