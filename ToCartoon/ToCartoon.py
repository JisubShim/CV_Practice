import cv2
# import numpy as np

# 이미지 로드
img = cv2.imread('image.jpg')

# 이미지를 그레이 스케일로 변환
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# median blur를 적용하여 노이즈 제거
gray = cv2.medianBlur(gray, 5)

# adaptive thresholding를 사용하여 edge를 찾음
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

# 이미지 컬러 변환
color = cv2.bilateralFilter(img, 9, 300, 300)

# 컬러 이미지와 edges mask 결합
cartoon = cv2.bitwise_and(color, color, mask=edges)

# 출력
cv2.imshow("Cartoon", cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()