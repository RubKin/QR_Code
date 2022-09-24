import numpy as np
import cv2
from pyzbar.pyzbar import decode
import os.path
from os import path

import os




cap = cv2.VideoCapture(0)
cap.set(3,1080)
cap.set(4,1940)

while True:

    success, img = cap.read()
    for barcode in decode(img):
        myData = barcode.data.decode("utf-8")
        print(myData)
        pts = np.array([barcode.polygon], np.int32)
        pts = pts.reshape((-1,1,2))
        cv2.polylines(img, [pts], True, (255,92, 0), 10)
        pts2 = barcode.rect
        cv2.putText(img, myData, (pts2[0], pts2[1]), cv2.FONT_ITALIC, 0.7, (255,92,0), 2)
    cv2.imshow('img',img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


#code = decode(img)
    # success, img = cap.read()
    # for barcode in decode(img):
    #     myData = barcode.data.decode('utf-8')
    #     print(myData)
    #     pts = np.array([barcode.polygon],np.int32)
    #     pts = pts.reshape((-1,1,2))
    #     cv2.polylines(img,[pts],True,(255,0,255),5)

    #     cv2.imshow("Result", img)
    #     cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()
#print (code)

# # import pyqrcode
# # from pyzbar.pyzbar import decode
# # from PIL import Image
# # qr = pyqrcode.create("HORN O.K. PLEASE.")
# # qr.png("horn.png", scale=6)
# # decode(Image.open('horn.png'))
# # print(qr.data)



