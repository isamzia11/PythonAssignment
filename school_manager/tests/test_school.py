import sys
from pathlib import Path

import pytest

# Make the "school" package importable no matter where pytest is run from
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from school.grades import average, grade
from school.manager import (
    add_student,
    add_marks,
    find_student,
    report_card,
    class_ranking,
)
from school.models import Student
from school.storage import save_students, load_students


# ---------- grades ----------

def test_average():
    assert average([80, 90, 85]) == 85


def test_average_empty_raises():
    with pytest.raises(ValueError):
        average([])


@pytest.mark.parametrize(
    "avg,expected",
    [
        (100, "A"),
        (80, "A"),
        (79, "B"),
        (70, "B"),
        (60, "C"),
        (33, "D"),
        (32, "Fail"),
        (0, "Fail"),
    ],
)
def test_grade(avg, expected):
    assert grade(avg) == expected


@pytest.mark.parametrize("avg", [-1, 101])
def test_grade_out_of_range(avg):
    with pytest.raises(ValueError):
        grade(avg)


# ---------- manager ----------

def test_add_student():
    students = []
    student = add_student(students, "Ali", 12)
    assert students == [student]
    assert student.name == "Ali"
    assert student.roll_number == 12
    assert student.marks == []


def test_add_student_duplicate_roll():
    students = []
    add_student(students, "Ali", 12)
    with pytest.raises(ValueError):
        add_student(students, "Sara", 12)


@pytest.mark.parametrize("name,roll", [("", 1), ("Ali", 0), ("Ali", -5)])
def test_add_student_invalid(name, roll):
    with pytest.raises(ValueError):
        add_student([], name, roll)


def test_add_marks():
    student = Student("Ali", 12)
    add_marks(student, 85)
    add_marks(student, 90)
    assert student.marks == [85, 90]


@pytest.mark.parametrize("mark", [-1, 101])
def test_add_marks_invalid(mark):
    student = Student("Ali", 12)
    with pytest.raises(ValueError):
        add_marks(student, mark)
    assert student.marks == []


def test_find_student():
    students = [Student("Ali", 12), Student("Sara", 7)]
    assert find_student(students, 7).name == "Sara"
    assert find_student(students, 99) is None


def test_report_card():
    student = Student("Ali", 12, [80, 90])
    card = report_card(student)
    assert "Ali" in card
    assert "Average: 85.00" in card
    assert "Grade: A" in card


def test_report_card_no_marks():
    card = report_card(Student("Ali", 12))
    assert "No marks recorded yet." in card


def test_class_ranking():
    students = [
        Student("Ali", 1, [60]),
        Student("Sara", 2, [95]),
        Student("Omar", 3),  # no marks, so left out
        Student("Zara", 4, [75]),
    ]
    ranked = class_ranking(students)
    assert [s.name for s in ranked] == ["Sara", "Zara", "Ali"]


# ---------- storage ----------

def test_save_and_load(tmp_path):
    file = tmp_path / "school.json"
    students = [Student("Ali", 12, [85, 91]), Student("Sara", 7)]

    save_students(students, file)
    loaded = load_students(file)

    assert [s.to_dict() for s in loaded] == [s.to_dict() for s in students]


def test_load_missing_file(tmp_path):
    assert load_students(tmp_path / "missing.json") == []


def test_load_corrupted_file(tmp_path):
    file = tmp_path / "school.json"
    file.write_text("this is not json")
    with pytest.raises(ValueError):
        load_students(file)
