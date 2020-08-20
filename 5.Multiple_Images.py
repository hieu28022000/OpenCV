import cv2
import numpy as np

# 1 vs 1
img_1 = cv2.imread('Img.jpg')
cap = cv2.VideoCapture('Vid.mp4')

sucess, img_2 = cap.read()
img_1 = cv2.resize(img_1,(300, 300), None)
img_2 = cv2.resize(img_2,(300, 300), None)

hor = np.hstack((img_1, img_2))
ver = np.vstack((img_1, img_2))

cv2.imshow('Hor', hor)
cv2.imshow('Ver', ver)

# cv2.waitKey(0)

# n vs n
path = 'Img.jpg'
kernel = np.ones((3, 3), np.uint8)

img = cv2.imread(path)
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 0 )
imgCanny = cv2.Canny(imgBlur, 80, 80)
imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)
imgEroded = cv2.erode(imgDilation, kernel, iterations=1)

# Fix size 
img1 = cv2.resize(img, (300, 300), None)
img2 = cv2.resize(imgGray, (300, 300), None)
img3 = cv2.resize(imgBlur, (300, 300), None)
img4 = cv2.resize(imgCanny, (300, 300), None)
img5 = cv2.resize(imgDilation, (300, 300), None)
img6 = cv2.resize(imgEroded, (300, 300), None)

# Fix color
img2 = cv2.cvtColor(img2, cv2.COLOR_GRAY2BGR)
img3 = cv2.cvtColor(img3, cv2.COLOR_GRAY2BGR)
img4 = cv2.cvtColor(img4, cv2.COLOR_GRAY2BGR)
img5 = cv2.cvtColor(img5, cv2.COLOR_GRAY2BGR)
img6 = cv2.cvtColor(img6, cv2.COLOR_GRAY2BGR)

hor_1 = np.hstack((img1, img2, img3))
hor_2 = np.hstack((img4, img5, img6))

ver = np.vstack((hor_1, hor_2))

cv2.imshow('2x3', ver)

cv2.waitKey(0) 