import qrcode
import random
from database import add_order

print("\n---- CASHIER ----")

while True:
    token = str(random.randint(1000, 9999))
    items = input("Enter items: ")
    amount = input("Enter amount: ")

    add_order(token, items, amount)

    qr = qrcode.make(token)
    fname = f"qr_{token}.png"
    qr.save(fname)
    qr.show()

    print("\nOrder Added!")
    print("Token:", token)

    again = input("Add another? (y/n): ")
    if again.lower() != 'y':
        break