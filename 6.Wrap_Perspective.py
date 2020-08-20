import cv2
import numpy as np

img = cv2.imread('Img.jpg')
cv2.imshow('Image', img)

# Set point normal
pts = np.float32([[400, 285], [475, 260], [425, 358], [495, 337]])
print(pts)
for i in range(0,4):
    cv2.circle(img, (pts[i, 0], pts[i, 1]), 1, (0, 0, 255), cv2.FILLED, 1)
cv2.imshow('Image', img)
#cv2.waitKey(0)


# Perspective
width, height = 300, 300
pts_fix = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
pts_mix = cv2.getPerspectiveTransform(pts, pts_fix)
img_output = cv2.warpPerspective(img, pts_mix, (width, height))
cv2.imshow('Output', img_output)
cv2.waitKey(0)