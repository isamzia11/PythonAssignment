
# Name Isam Zia Roll no: TRN-2026-00346

percentage = float(input("Enter percentage: "))

if percentage < 0 or percentage > 100:
    print("Invalid percentage!")

elif percentage >= 90:
    print("Grade: A+")
    print("Status: Pass")

elif percentage >= 80:
    print("Grade: A")
    print("Status: Pass")

elif percentage >= 70:
    print("Grade: B")
    print("Status: Pass")

elif percentage >= 60:
    print("Grade: C")
    print("Status: Pass")

elif percentage >= 50:
    print("Grade: D")
    print("Status: Pass")

else:
    print("Grade: F")
    print("Status: Fail")
