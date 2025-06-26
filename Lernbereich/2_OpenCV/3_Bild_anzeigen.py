import cv2, os

ery_image = cv2.imread(
    "OpenCV/Folder/ery.png"
)  # ery_image als kopie im RAM gespeichert
ery_gray = cv2.imread(
    "OpenCV/Folder/ery.png", cv2.IMREAD_GRAYSCALE
)  # mit flag, gray-scale

skaliert = cv2.resize(ery_image, None, fx=0.5, fy=0.5)  # ery_image auf 50% skaliert
scale = cv2.resize(ery_gray, (720, 480))  # ery_gray wird auf feste Skalierung geändert

cv2.imshow("Erythrozyten", skaliert)
cv2.imshow("GRAU", scale)
cv2.waitKey(0)
cv2.destroyAllWindows()
