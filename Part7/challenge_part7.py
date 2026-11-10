# Name Isam Zia Roll no: TRN-2026-00346 


import csv
import json

results = {
    "Ali": [80, 72, 91],
    "Sara": [95, 88, 90],
    "Ahmed": [55, 38, 62],
    "Zara": [78, 81, 84],
    "Hamza": [65, 70, 75]
}

# Save CSV
with open("results.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow([
        "Name", "Mark1", "Mark2", "Mark3", "Average"
    ])

    for name, marks in results.items():
        avg = sum(marks) / len(marks)

        writer.writerow([
            name, marks[0], marks[1], marks[2], avg
        ])

print("CSV saved successfully!")

# Save JSON
with open("results.json", "w", encoding="utf-8") as file:
    json.dump(results, file, indent=4)

print("JSON saved successfully!")
