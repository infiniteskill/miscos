import cv2
img=cv2.imread('img2/11.jpg')
drimg=cv2.imread('blank.jpg')
drimg = cv2.resize(drimg, (0,0), fx=2, fy=2)
img = cv2.resize(img, (0,0), fx=2, fy=2)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray_img, 127, 500, 1)
cv2.imshow("thresh",thresh)
contours , _= cv2.findContours(thresh, cv2.RETR_TREE, 1)

cnt = contours
for i in range(len(contours)):

    #---- Mark contours above certain area ----
    if (cv2.contourArea(cnt[i]) > 1000):
        final_image = cv2.drawContours(drimg, cnt[i], 1, (0,0,0), 1)
        
        cv2.fillPoly(drimg, pts =[cnt[i]], color=(0,0,255))

cv2.imshow('Marked image', drimg )
cv2.waitKey(0)
cv2.destroyAllWindows()
