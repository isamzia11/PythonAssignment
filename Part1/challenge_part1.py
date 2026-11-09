# Name Isam Zia Roll no: TRN-2026-00346 

celsius = float(input("Enter Celsius: "))
km = float(input("Enter kilometers: "))

fahrenheit = celsius * 9 / 5 + 32
kelvin = celsius + 273.15
miles = km * 0.621371
metres = km * 1000

print(f"Fahrenheit: {fahrenheit:.1f}")
print(f"Kelvin: {kelvin:.1f}")
print(f"Miles: {miles:.1f}")
print(f"Metres: {metres:.1f}")