import cv2, os

os.makedirs("OpenCV/Folder/Exports", exist_ok=True)
pfad = os.path.join("OpenCV", "Folder", "Exports", "ery_gray.png")

ery_gray = cv2.imread("OpenCV/Folder/ery.png", cv2.IMREAD_GRAYSCALE)
cv2.imwrite(pfad, ery_gray)
