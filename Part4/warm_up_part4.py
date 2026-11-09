# Name Isam Zia Roll no: TRN-2026-00346 

items = ["milk", "bread", "eggs"]

items.append("tea")
items.remove("bread")
items.sort()

for number, item in enumerate(items, start=1):
    print(f"{number}. {item}")

