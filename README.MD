# QR-Based Self-Service Stall Order System

A Python-based system to manage orders at a self-service stall using QR codes. Customers receive a QR for their order, staff mark orders as ready, and pickup is tracked via QR scanning.  

---

## Features

- **Order Management:** Add orders with items and amount.  
- **QR Code Generation:** Each order gets a unique QR for identification.  
- **Status Tracking:** Orders marked as `READY` by staff.  
- **Display:** Shows ready orders once to avoid repetition.  
- **Pickup:** Customers scan QR to collect and remove orders from the system.  
- **Database:** SQLite (`orders.db`) stores all orders with token, items, amount, and status.  

---

## Modules

| File | Description |
|------|-------------|
| `database.py` | Manages orders in the database. |
| `cashier.py` | Add orders and generate QR codes. |
| `kitchen.py` | Mark pending orders as ready. |
| `display.py` | Display ready orders once. |
| `pickup.py` | Scan QR codes to complete orders. |

---

## Installation

1. **Clone the repository**
```bash
git clone <repository_url>
cd <repository_folder>

2. Install dependencies



pip install qrcode opencv-python pyzbar

3. Run modules



python cashier.py      # Add new orders
python kitchen.py      # Mark orders ready
python display.py      # Show ready orders
python pickup.py       # Scan QR and complete order


---

How it Works

1. Cashier adds a new order → QR code generated → stored in database.


2. Staff marks orders as ready → status updated in database.


3. Display screen shows ready orders → each order shown only once.


4. Customers scan QR code at pickup → order removed from database after collection.




---

Notes

Python 3.x required.

Camera needed for QR scanning.

orders.db is automatically created in the project folder.



---

Author

Kritika Aryan