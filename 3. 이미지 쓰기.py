# -*-coding: utf-8 -*-

import numpy as np
import cv2

img = cv2.imread('IU.jpg', 0)
cv2.imshow('image', img)
# 만약 운영체제가 64bit이면, k = cv2.waitKey(0) & 0xFF 해줘야한다.
k = cv2.waitKey(0)

if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('IUgrey.jpg', img)
    cv2.destroyAllWindows()