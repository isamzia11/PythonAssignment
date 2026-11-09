# Name Isam Zia Roll no: TRN-2026-00346 

results = {
        "Ali": [80, 72, 91],
        "Sara": [95, 88, 90],
        "Ahmed": [55, 38, 62],
        "Zara": [78, 81, 84],
        "Hamza": [65, 70, 75]
    }

averages = {}
failed_students = set()

print("===== CLASS RESULT SHEET =====")

for name, marks in results.items():
    total = sum(marks)
    avg = total / len(marks)

    averages[name] = avg

    print(
        f"{name} | Total: {total} | "
        f"Average: {avg:.2f}"
    )

    if any(mark < 40 for mark in marks):
        failed_students.add(name)

topper = max(averages, key=averages.get)

print(f"\nClass Topper: {topper}")
print(f"Students below 40: {failed_students}")

