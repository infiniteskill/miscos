import io
import json
import cv2
import numpy as np
import requests
img = cv2.imread("img2/0.jpg")
height, width, _ =img.shape
url_api = "https://api.ocr.space/parse/image"
_, compressedimage = cv2.imencode(".jpg", img)
file_bytes = io.BytesIO(compressedimage)

result = requests.post(url_api,
                  files = {"screenshot.jpg": file_bytes},
                  data = {"apikey": "helloworld",
                          "language": "eng"})

result = result.content.decode()
result = json.loads(result)
numberplate=result['ParsedResults'][0]['ParsedText']
print(numberplate)