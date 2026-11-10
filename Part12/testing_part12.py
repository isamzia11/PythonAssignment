
marks = [90, 25, 70]
passing = []

# Bug 1 fixed:
# Iterate over every mark, including the last one.
for m in range(len(marks)):

    if marks[m] > 33:

        # Bug 2 fixed:
        # Append instead of replacing the list.
        passing.append(marks[m])

# Bug 3 fixed:
# Divide by the number of passing marks.
if passing:
    average = sum(passing) / len(passing)
    print("Average:", average)
else:
    print("No passing marks")
