def average(marks):
    """Return the average of a list of marks."""
    if not marks:
        raise ValueError("marks list cannot be empty")
    return sum(marks) / len(marks)


def grade(avg):
    """Return the letter grade for an average between 0 and 100."""
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
