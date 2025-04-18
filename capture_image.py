import cv2

# Open the webcam (0 is the default camera)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Cannot open webcam")
    exit()

print("📷 Press SPACE to capture a frame. Press ESC to exit.")

while True:
    ret, frame = cap.read()

    if not ret:
        print("⚠️ Failed to grab frame")
        break

    # Show the live video
    cv2.imshow("Live Feed - Press SPACE to capture", frame)

    key = cv2.waitKey(1)
    if key % 256 == 27:  # ESC key to exit
        print("🛑 Escape hit, closing...")
        break
    elif key % 256 == 32:  # SPACE key to capture
        img_name = "frame.jpg"
        cv2.imwrite(img_name, frame)
        print(f"✅ Image saved as {img_name}")
        break

cap.release()
cv2.destroyAllWindows()
