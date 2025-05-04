num_items = int(input("Enter the number of different items: "))
total = 0
for i in range(1, num_items + 1):
    print(f"\nItem {i}:")
    price = float(input("  Enter price of the item: ₹"))
    quantity = int(input("  Enter quantity: "))
    total += price * quantity
gst = total * 0.18
grand_total = total + gst
print("\n Final Bill ")
print(f"Subtotal: ₹{total:.2f}")
print(f"GST (18%): ₹{gst:.2f}")
print(f"Total Amount to Pay: ₹{grand_total:.2f}")

