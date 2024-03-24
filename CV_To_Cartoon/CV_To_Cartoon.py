import cv2

min_threshold = 10
max_threshold = 150

# 이미지 로드
img = cv2.imread('image1.jpg') # 증명사진
# img = cv2.imread('image2.jpg') # 학교 풍경 사진

# gray scale로 변환
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# median blur로 노이즈 제거
gray = cv2.medianBlur(gray, 7)

# Canny edge detector을 통해 이미지의 가장자리 찾기
edge = 255 - cv2.Canny(img, min_threshold, max_threshold)  # Canny edge detect 결과를 반전시킴
edge = cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR)  # edge 이미지를 3채널로 변환

# 이미지 컬러 변환 (bilateral 필터를 사용하여 노이즈 제거하면서 엣지 보존)
color = cv2.bilateralFilter(img, -1, 10, 10)

# color 이미지와 edge를 결합하여 카툰 효과 생성
cartoon = cv2.bitwise_and(color, edge)

# 출력
cv2.imshow("Cartoon", cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()