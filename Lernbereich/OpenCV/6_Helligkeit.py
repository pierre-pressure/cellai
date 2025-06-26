import cv2, os

pfad = os.path.join("OpenCV", "Folder", "Exports", "ery_grau.png")
os.makedirs("OpenCV/Folder/Exports", exist_ok=True)

ery_gray = cv2.imread("OpenCV/Folder/Exports/ery_gray.png")
ery_grau = cv2.add(ery_gray, 50)
cv2.imwrite(pfad, ery_grau)
