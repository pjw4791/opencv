# -*-coding: utf-8 -*-

import numpy as np
import cv2

# 회색(gray)으로 이미지 읽기
img = cv2.imread('IU.jpg', 0)

# 원색으로 이미지 읽기
# img = cv2.imread('IU.jpg', 1)


# cv2.imshow('새 창에 나타날 이름', cv2.imread('IU.jpg', 0))
cv2.imshow('IUimage', img)
# cv2.waitKey()는 지정된 시간동안 키보드 입력을 기다리는 함수 1/1000초(=ms)
# cv2.waitKey(0)은 키보드 입력이 있을때까지 기다리라
# cv2.waitKey(1000)은 1초간 기다리라
cv2.waitKey(10000)
cv2.destroyAllWindows()