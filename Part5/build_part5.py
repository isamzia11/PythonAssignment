
def average(marks):
    if not marks:
        raise ValueError("Marks list cannot be empty")

    return sum(marks) / len(marks)


def grade(avg):
    if avg < 0 or avg > 100:
        raise ValueError("Average must be 0-100")

    if avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 33:
        return "D"
    else:
        return "Fail"


def report(name, marks):
    avg = average(marks)
    student_grade = grade(avg)

    return (
        f"{name} | Average: {avg:.2f} | "
        f"Grade: {student_grade}"
    )


students = {
    "Ali": [85, 80, 90],
    "Sara": [95, 88, 92],
    "Ahmed": [45, 55, 60]
}

print("===== STUDENT REPORTS =====")

for name, marks in students.items():
    print(report(name, marks))
