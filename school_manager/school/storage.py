import json
from pathlib import Path

from school.models import Student


def save_students(students, filename):
    """Write all students to a JSON file."""
    data = [student.to_dict() for student in students]
    Path(filename).write_text(json.dumps(data, indent=2), encoding="utf-8")


def load_students(filename):
    """Read students from a JSON file. A missing file means no students yet."""
    path = Path(filename)
    if not path.exists():
        return []

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        return [Student.from_dict(item) for item in data]
    except (json.JSONDecodeError, KeyError, TypeError) as error:
        raise ValueError(f"{filename} is corrupted: {error}") from error
