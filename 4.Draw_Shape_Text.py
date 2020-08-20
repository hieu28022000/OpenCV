import cv2
import numpy as np

# Create matrix
img = np.zeros((300, 300, 3), np.uint8)

# Load color
img[:] = (150, 150, 0)
cv2.imshow('Image', img)

# Draw line
cv2.line(img,(0,0),(130,130),(0,200,200),2)
cv2.line(img,(130,130),(210,80),(0,200,200),2)
cv2.imshow('Line',img)

# Draw rectangle
cv2.rectangle(img, (210,80), (260,30), (0,200,200), cv2.FILLED)
cv2.imshow('Rectangle', img)

# Draw circle
cv2.circle(img, (130, 155), 25, (0, 200, 200), cv2.FILLED)
cv2.imshow('Circle', img)

# Draw text 
cv2.putText(img, 'Draw text', (50, 220), cv2.FONT_HERSHEY_COMPLEX,1, (0, 0, 0))
cv2.imshow('Draw text', img)

cv2.waitKey(0)