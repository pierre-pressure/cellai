import cv2

cap = cv2.VideoCapture(1) 

if not cap.isOpened():
    print("Kamera konnte nicht geöffnet werden.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Kein Bild erhalten.")
        break

    cv2.imshow("Live View (Surface Kamera)", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
