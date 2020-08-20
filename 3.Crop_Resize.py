import cv2

img = cv2.imread('Img.jpg')
img_Resize = cv2.resize(img, (500, 500))
img_Crop = img_Resize[100:301, 150:351]

cv2.imshow('Normal', img)
cv2.imshow('Resize', img_Resize)
cv2.imshow('Crop', cv2.resize(img_Crop,(500,500)))

cv2.waitKey(3000)