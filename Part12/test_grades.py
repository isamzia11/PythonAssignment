

import sys
from pathlib import Path

import pytest

# build_part5.py lives in the Part5 folder, so add it to the import path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "Part5"))

from build_part5 import grade


@pytest.mark.parametrize(
    "marks,expected",
    [
        (32, "Fail"),
        (33, "D"),
        (59, "D"),
        (60, "C"),
        (69, "C"),
        (70, "B"),
        (79, "B"),
        (80, "A"),
    ]
)
def test_grade_boundaries(marks, expected):
    assert grade(marks) == expected


def test_invalid_high_marks():
    with pytest.raises(ValueError):
        grade(101)


def test_invalid_negative_marks():
    with pytest.raises(ValueError):
        grade(-1)
