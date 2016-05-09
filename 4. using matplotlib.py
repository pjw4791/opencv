# -*-coding: utf-8 -*-

import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('IU.jpg', 0)
'''
opencv는 BGR모드로 컬러 이미지를 다루는데 반해 Matplotlib은 RGB모드로 컬러 이미지를 다룬다.
따라서, opencv로 읽어들인 컬러 이미지 객체를 matplotlib에 그대로 사용하게 될 때 제대로 된 컬러 색상이 나오지 않는다.
'''
plt.imshow(img, cmap='gray', interpolation='bicubic')
# plt.imshow(img, interpolation='bicubic')
# plt.imshow(img, cmap='gray')
# plt.imshow(img)
plt.xticks([]), plt.yticks([]) # to hide tick values on X and Y axis
plt.show()