import cv2
import numpy as np

path = 'Img.jpg'
kernel = np.ones((3, 3), np.uint8)

image = cv2.imread(path)

img = cv2.resize(image, (500, 500))
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 0 )
imgCanny = cv2.Canny(imgBlur, 80, 80)
imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)
imgEroded = cv2.erode(imgDilation, kernel, iterations=1)

cv2.imshow('Normal',img)
cv2.imshow('Gray',imgGray)
cv2.imshow('Blur', imgBlur)
cv2.imshow('Canny', imgCanny)
cv2.imshow('Dilation', imgDilation)
cv2.imshow('Eroded', imgEroded)

cv2.waitKey(0)
