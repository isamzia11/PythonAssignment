
# 1. Squares from 1 to 10
squares = [n ** 2 for n in range(1, 11)]

# 2. Names longer than four letters
names = ["Ali", "Sara", "Ahmed", "Hamza", "Zara"]
long_names = [name for name in names if len(name) > 4]

# 3. Student averages
results = {
    "Ali": [80, 72, 91],
    "Sara": [95, 88, 90],
    "Ahmed": [55, 38, 62],
    "Zara": [78, 81, 84],
    "Hamza": [65, 70, 75]
}

averages = {
    name: sum(marks) / len(marks)
    for name, marks in results.items()
}

# 4. Passing students
passing = [
    name
    for name, avg in averages.items()
    if avg >= 33
]

print("Squares:", squares)
print("Long Names:", long_names)
print("Averages:", averages)
print("Passing:", passing)
