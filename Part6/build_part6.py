# Name Isam Zia Roll no: TRN-2026-00346 

def buggy_add_item(item, cart=[]):
    cart.append(item)
    return cart


print("===== BUGGY FUNCTION =====")

customer1 = buggy_add_item("Apple")
customer2 = buggy_add_item("Banana")

print("Customer 1:", customer1)
print("Customer 2:", customer2)


# Correct version
def add_item(item, cart=None):
    if cart is None:
        cart = []

    cart.append(item)
    return cart


print("\n===== CORRECT FUNCTION =====")

customer1 = add_item("Apple")
customer2 = add_item("Banana")

print("Customer 1:", customer1)
print("Customer 2:", customer2)

# Same customer's existing cart
customer1 = add_item("Milk", customer1)
print("Customer 1 updated:", customer1)
