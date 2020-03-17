import os
from google.cloud import vision_v1p3beta1 as vision

import cv2


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'client_key.json'


SOURCE_PATH = "img2/"

# SOURCE_PATH = "img2/"
def recognize_license_plate(img_path):

    img = cv2.imread(img_path)

    height, width = img.shape[:2]

    client = vision.ImageAnnotatorClient()

    with open(img_path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
  
    for i in range(1):
        print(texts[0].description)


print('---------- Start recognize license palate --------')
path = SOURCE_PATH + '0.jpg'
recognize_license_plate(path)
print('---------- End ----------')



