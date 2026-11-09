i

tem = input("Enter item name: ")
price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))

subtotal = price * quantity
discount = subtotal * 0.05
discounted_amount = subtotal - discount
tax = discounted_amount * 0.17
final_total = discounted_amount + tax

print("\n======= SHOP BILL =======")
print(f"Item: {item}")
print(f"Subtotal: Rs {subtotal:.2f}")
print(f"Discount: Rs {discount:.2f}")
print(f"Tax: Rs {tax:.2f}")
print(f"Final Total: Rs {final_total:.2f}")