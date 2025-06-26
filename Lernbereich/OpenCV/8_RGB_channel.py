import os, cv2

pfad = os.path.join("OpenCV", "Folder", "Exports", "ery_gray_rgb.png")
ery_rgb = cv2.imread("OpenCV/Folder/ery.png")
b, g, r = cv2.split(ery_rgb)

# Helligkeit durch rot-stärke bestimmt | Graubild
zero = cv2.merge([r, r, r])
cv2.imwrite(pfad, zero)

# Nur rot
pfad = os.path.join("OpenCV", "Folder", "Exports", "ery_only_rgb.png")
nur_rot = cv2.merge(
    [b * 0, g * 0, r]
)  # G/B-Anteile auf 0, R-Anteile bleiben -> deswegen rötlich [0, 0, r]
cv2.imwrite(pfad, nur_rot)
