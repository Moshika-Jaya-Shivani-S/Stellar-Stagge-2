import cv2
img = cv2.imread("nature.jpg")
cv2.imshow("window",img)
cv2.waitKey(0)
print(img)
gray_img=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.imshow("window",gray_img)
cv2.waitKey(0)