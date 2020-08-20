import cv2

#Image
img = cv2.imread('Img.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('xinh nhiều', img)
cv2.waitKey(0)
cv2.imshow('xinh sơ sơ', img_gray)
cv2.waitKey(0)

#Video
frameWidth = 900
frameHeight = 500

cap = cv2.VideoCapture('Vid.mp4')
#cap = cv2.VideoCapture(0)

while True:
    sucess, img = cap.read()
    img = cv2.resize(img,(frameWidth, frameHeight))
    cv2.imshow('Xấu như chó', img)

    if (cv2.waitKey(0) & 0xFF == ord('q')):
        break