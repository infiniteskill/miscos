import cv2
import pytesseract
import sys
import numpy as np



img=cv2.imread('imgs/day/1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
contours, hierarchy=cv2.findContours(gray,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
cv2.drawContours(gray,contours,-1,(0,255,0),1)

ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
k = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]], np.uint8)
# closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, k)
k1 = np.ones((3, 3), np.uint8)

# erosion = cv2.erode(thresh, k1, iterations = 1)
# dialation=cv2.dilate(thresh, k1, iterations=1) 


cv2.imshow('thresh',thresh)
cv2.cv2.waitKey(0)


text=pytesseract.image_to_string(thresh)

with open('text.txt','w') as f:
    f.write(text)










print(text)