class Student:
    def __init__(self, name, roll_number, marks=None):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks if marks is not None else []

    def to_dict(self):
        return {
            "name": self.name,
            "roll_number": self.roll_number,
            "marks": self.marks,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["roll_number"], list(data.get("marks", [])))

    def __str__(self):
        return f"{self.name} (Roll {self.roll_number})"
