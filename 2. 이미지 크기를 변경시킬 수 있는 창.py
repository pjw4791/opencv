# -*-coding: utf-8 -*-

import numpy as np
import cv2

img = cv2.imread('IU.jpg', 0)

# 윈도우 사이즈 조절 가능
cv2.namedWindow('IUimage', cv2.WINDOW_NORMAL)
cv2.imshow('IUimage', img)

cv2.waitKey(0)
cv2.destroyAllWindows()