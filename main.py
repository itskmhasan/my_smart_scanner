import urllib.request as request
import numpy as np
import cv2

url = 'https://192.168.1.90:8080/shot.jpg'
while True:
    img = request.urlopen(url)
    img_bytes = bytearray(img.read())
    img_np = np.array(img_bytes, dtype=np.uint8)
    frame = cv2.imdecode(img_np, 0)
    cv2.imshow('My Smart Scanner', frame)
    cv2.waitKey(1)
