import numpy as np
import cv2
from matplotlib import pyplot as plt

# img = cv2.imread('shrek.jpeg')

cap=cv2.VideoCapture('dore.mp4')
x1, x2, y1, y2 = 100, 600, 100, 600

while True:
    _,img=cap.read()
    # img = img[y1:y2, x1:x2]
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # gray=cv2.GaussianBlur(gray,(7,7),0) 
    ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

      # noise removal
    kernel = np.ones((3,3),np.uint8)
    opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 1)

    # sure background area
    sure_bg = cv2.dilate(opening,kernel,iterations=0)

    # Finding sure foreground area
    dist_transform = cv2.distanceTransform(sure_bg,cv2.DIST_L2,5)
    ret, sure_fg = cv2.threshold(dist_transform,0.85*dist_transform.max(),255,0)

    # Finding unknown region
    sure_fg = np.uint8(sure_fg)
    unknown = cv2.subtract(sure_bg,sure_fg)

    # Marker labelling
    ret, markers = cv2.connectedComponents(sure_fg)

    # Add one to all labels so that sure background is not 0, but 1
    markers = markers+1

    # Now, mark the region of unknown with zero
    markers[unknown==255] = 0
    markers = cv2.watershed(img,markers)
    img[markers == -1] = [255,0,0]
    font = cv2.FONT_HERSHEY_SIMPLEX
    labeled_img=cv2.putText(img, "Count = {}".format(ret-1), (10, 40), font, 0.5, (0, 255, 0), 1, cv2.LINE_AA)

    cv2.imshow("none",labeled_img)
    

    if cv2.waitKey(25) & 0xFF == ord('q'):
      break
cap.release()
cv2.destroyAllWindows()
