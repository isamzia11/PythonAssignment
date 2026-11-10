# Name Isam Zia Roll no: TRN-2026-00346 

class Student:
    def __init__(self, name, roll_number, marks=None):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks if marks is not None else []

    def add_mark(self, mark):
        self.marks.append(mark)

    def average(self):
        if not self.marks:
            return 0.0

        return sum(self.marks) / len(self.marks)

    def __str__(self):
        return (
            f"{self.name} (Roll {self.roll_number}): "
            f"avg {self.average():.1f}"
        )


student1 = Student("Ali", 12)

student1.add_mark(80)
student1.add_mark(82)
student1.add_mark(81)

print(student1)
