import cv2

# LOAD AN IMAGE USING 'IMREAD'
img = cv2.imread("face.jpg")

# DISPLAY
cv2.imshow("face", img)
cv2.waitKey(0)