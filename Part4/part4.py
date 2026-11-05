
# Name Isam Zia Roll no: TRN-2026-00346

subjects = ("Math", "English", "Science")

students = [
    {
        "id": 101,
        "name": "Ali",
        "class": "10A",
        "marks": [90, 85, 95]
    },
    {
        "id": 102,
        "name": "Sara",
        "class": "10A",
        "marks": [95, 90, 92]
    },
    {
        "id": 103,
        "name": "Ahmed",
        "class": "10B",
        "marks": [70, 75, 80]
    }
]

unique_classes = {
    student["class"] for student in students
}

print("Subjects:", subjects)

print("\n===== STUDENT RECORDS =====")

for student in students:
    print("ID:", student["id"])
    print("Name:", student["name"])
    print("Class:", student["class"])
    print("Marks:", student["marks"])
    print("-------------------------")

print("Unique Classes:", unique_classes)
