# Name Isam Zia Roll no: TRN-2026-00346 
import csv

topper_name = None
highest_average = -1

with open("results.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        name = row["Name"]
        avg = float(row["Average"])

        if avg > highest_average:
            highest_average = avg
            topper_name = name

if topper_name is None:
    print("No student records found.")
else:
    print("Class Topper:", topper_name)
    print(f"Highest Average: {highest_average:.2f}")
