import os, cv2

pfad = os.path.join("OpenCV", "Folder", "Exports", "ery_contrast.png")

ery_gray = cv2.imread("OpenCV/Folder/ery.png")
contrast_img = cv2.convertScaleAbs(
    ery_gray, alpha=1.3, beta= -10
)  # alpha: Kontrastfaktor | beta: Helligkeitsfaktor | convertScaleAbs: lineare Transformation
cv2.imwrite(pfad, contrast_img)
