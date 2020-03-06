import cv2
import pytesseract
import sys


img=cv2.imread('rec.jpg')
text=pytesseract.image_to_string(img)

with open('text.txt','w') as f:
    f.write(text)
amt='AMOUNT'.casefold()
total='TOTAL'.casefold()
total_amt="TOTAL AMOUNT".casefold()
text=text.casefold()
if (text.find(amt)>0):
    i=text.find(amt)
    print("Bill is",text[i:i+15])

elif (text.find(total)>0):
    i=text.find(total)
    print("Bill is",text[i:i+15])

elif(text.find(total_amt)>0):
    i=text.find(total_amt)
    print("Bill is",text[i:i+10])