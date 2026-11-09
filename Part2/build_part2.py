# Name Isam Zia Roll no: TRN-2026-00346 

marks = float(input("Enter marks: "))

if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 80:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 33:
    print("Grade D")
else:
    print("Fail")