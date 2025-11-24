from database import get_pending, set_ready

print("\n---- KITCHEN ----")

while True:
    pending = get_pending()

    if not pending:
        print("No pending orders.")
    else:
        print("\nPending Orders:")
        for tok, item in pending:
            print(f"{tok} --> {item}")

        token = input("\nEnter token to mark READY: ")
        set_ready(token)
        print("Order marked READY!")

    again = input("Update more? (y/n): ")
    if again.lower() != "y":
        break