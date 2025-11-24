import time
from database import get_ready

print("\n---- DISPLAY SCREEN ----")
shown = set()     # ensures each token shows ONCE

while True:
    ready = get_ready()

    for tok, item in ready:
        if tok not in shown:
            print(f"ORDER READY → Token: {tok} | Items: {item}")
            shown.add(tok)

    time.sleep(2)