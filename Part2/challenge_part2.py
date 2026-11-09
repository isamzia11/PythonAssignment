# Name Isam Zia Roll no: TRN-2026-00346

units = int(input("Enter units: "))

if units < 0:
    print("Invalid units")
else:
    if units <= 100:
        bill = units * 10

    elif units <= 200:
        bill = 100 * 10 + (units - 100) * 15

    else:
        bill = 100 * 10 + 100 * 15 + (units - 200) * 20

    bill += 50
    print(f"Total Bill: Rs {bill}")