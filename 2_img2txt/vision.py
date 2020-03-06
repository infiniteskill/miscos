import cv2
import pytesseract
import sys


img=cv2.imread('img3.png')
text=pytesseract.image_to_string(img)

with open('text.txt','w') as f:
    f.write(text)
print(text)
