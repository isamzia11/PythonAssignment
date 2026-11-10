def attendance_percentage(present, total):
    if total <= 0:
        raise ValueError("Total days must be positive")
    return present / total * 100