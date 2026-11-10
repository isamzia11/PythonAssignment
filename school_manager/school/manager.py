from school.grades import average, grade
from school.models import Student


def add_student(students, name, roll):
    """Create a student and add it to the list. Raises ValueError on bad input."""
    if not name:
        raise ValueError("name cannot be empty")
    if roll <= 0:
        raise ValueError("roll number must be positive")
    if find_student(students, roll) is not None:
        raise ValueError(f"roll number {roll} already exists")

    student = Student(name, roll)
    students.append(student)
    return student


def add_marks(student, mark):
    """Add one mark (0-100) to a student."""
    if mark < 0 or mark > 100:
        raise ValueError("mark must be between 0 and 100")
    student.marks.append(mark)


def find_student(students, roll):
    """Return the student with this roll number, or None."""
    for student in students:
        if student.roll_number == roll:
            return student
    return None


def report_card(student):
    """Return a printable report card for one student."""
    lines = [
        "===== REPORT CARD =====",
        f"Name: {student.name}",
        f"Roll: {student.roll_number}",
    ]

    if not student.marks:
        lines.append("No marks recorded yet.")
    else:
        avg = average(student.marks)
        marks_text = ", ".join(f"{m:g}" for m in student.marks)
        lines.append(f"Marks: {marks_text}")
        lines.append(f"Average: {avg:.2f}")
        lines.append(f"Grade: {grade(avg)}")

    return "\n".join(lines)


def class_ranking(students):
    """Return students that have marks, highest average first."""
    with_marks = [s for s in students if s.marks]
    return sorted(with_marks, key=lambda s: average(s.marks), reverse=True)
