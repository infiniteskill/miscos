import cv2
import numpy as np

original=cv2.imread("md.jpeg")

gray_im = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)

gray_correct = np.array(255 * (gray_im / 255) ** 1.2 , dtype='uint8')

# gray_equ = cv2.equalizeHist(gray_im)


thresh = cv2.adaptiveThreshold(gray_correct, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 255, 19)
thresh = cv2.bitwise_not(thresh)


kernel = np.ones((15,15), np.uint8)
img_dilation = cv2.dilate(thresh, kernel, iterations=0)
# img_erode = cv2.erode(img_dilation,kernel, iterations=1)

img_erode = cv2.medianBlur(img_dilation, 9)

ret, labels = cv2.connectedComponents(img_erode)
label_hue = np.uint8(179 * labels / np.max(labels))
blank_ch = 255 * np.ones_like(label_hue)
labeled_img = cv2.merge([label_hue, blank_ch, blank_ch])
labeled_img = cv2.cvtColor(labeled_img, cv2.COLOR_HSV2BGR)
labeled_img[label_hue == 0] = 0
font = cv2.FONT_HERSHEY_SIMPLEX
labeled_img=cv2.putText(labeled_img, "Count = {}".format(ret-1), (10, 40), font, 0.5, (0, 255, 0), 1, cv2.LINE_AA)
print('objects number is:', ret-1)

cv2.imshow('gra',labeled_img)




cv2.waitKey(0)
cv2.destroyAllWindows()