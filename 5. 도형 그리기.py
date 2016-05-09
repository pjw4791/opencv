# -*-coding: utf-8 -*-

import numpy as np
import cv2

# Create a black image
# 512*512 크기의 검정색 이미지를 생성한 것과 같다.(B, G, R)=(0, 0, 0)
# 데이터 타입이 uint8
img = np.zeros((512, 512, 3), np.uint8)

'''
Draw a diagonal blue line with thickness of 5 px
img : 직선을 그릴 그림판 / (0, 0) : 직선의 시작점 / (511,511) : 직선의 끝점
(255,0,0) : BGR값으로 선의 색상
5 : 선의 굵기
'''
img = cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)

'''
img : 직사각형을 그릴 그림판 / (384, 0) : 좌상 / (510,128) : 우하
(0,255,0) : BGR값으로 선의 색상
3 : 선의 굵기
'''
img = cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)

'''
img : 원을 그릴 그림판 / (447, 63) : 원의 중심 / 63 : 원의 반지름
(0,0,255) : BGR값으로 선의 색상
-1 : 주어진 색상으로 도형을 채움
'''
img = cv2.circle(img, (447, 63), 63, (0, 0, 255), -1)

'''
img : 타원을 그릴 그림판 / (256, 256) : 타원의 중심 / (100, 50) : 장축과 단축의 1/2 길이
0,0,180 : 타원의 기울기 각도, 타원 호를 그리는 시작 각도, 타원 호를 그리는 끝 각도
(255,0,0) : BGR값으로 선의 색상
-1 : 주어진 색상으로 도형을 채움
'''
img = cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 180, (255, 0, 0), -1)


pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
# pts = pts.reshape(-1, 1, 2)
img = cv2.polylines(img, [pts], True, (0, 255, 255))
# 마지막에 처음과 안 이어주는 것이 False
# img = cv2.polylines(img, [pts], False, (0, 255, 255))

font = cv2.FONT_HERSHEY_SIMPLEX
# 4:폰트크기, 2:굵기
cv2.putText(img, 'OpenCV', (10, 500), font, 4, (255, 255, 255), 2, cv2.LINE_AA)

cv2.imshow('drawing', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
