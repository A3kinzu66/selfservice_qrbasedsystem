from database import set_picked, get_ready
import cv2
import time

print("\n---- PICKUP COUNTER ----")

def scan_qr():
    cap = cv2.VideoCapture(0)  # open default camera
    detector = cv2.QRCodeDetector()

    print("Scanning QR code... Press 'q' to quit.")

    token = None
    while True:
        ret, frame = cap.read()
        if not ret:
            continue

        # detect and decode QR code
        data, bbox, _ = detector.detectAndDecode(frame)
        if bbox is not None:
            # draw bounding box
            n_lines = len(bbox)
            for i in range(n_lines):
                pt1 = tuple(map(int, bbox[i][0]))
                pt2 = tuple(map(int, bbox[(i + 1) % n_lines][0]))
                cv2.line(frame, pt1, pt2, (0, 255, 0), 2)

            if data:
                token = data
                cv2.putText(frame, token, (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                            1, (0, 255, 0), 2)
                print(f"Scanned token: {token}")
                time.sleep(1)
                break

        cv2.imshow("Pickup Scanner", frame)

        # quit camera manually
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    return token

while True:
    ready = get_ready()

    if not ready:
        print("No READY orders.")
    else:
        print("\nREADY FOR PICKUP:")
        for tok, item in ready:
            print(f"{tok} --> {item}")

        token = scan_qr()
        if token:
            set_picked(token)
            print("Order picked & removed!")

    again = input("\nNext? (y/n): ")
    if again.lower() != "y":
        break