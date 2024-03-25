# CV_To_Cartoon
OpenCV를 통해 카툰 필터를 구현해 보았습니다.

#### 이 알고리즘으로 만화 같은 느낌이 잘 표현되는 사진
![스크린샷 2024-03-24 162201](https://github.com/JisubShim/CV_Practice/assets/118372554/18b54fe8-785d-415f-b2c8-20696748db26)<br>
사진출처 : https://www.seoultech.ac.kr/intro/campinfo/camper/information/
<br>
#### 이 알고리즘으로 만화 같은 느낌이 잘 표현되지 않는 사진
![스크린샷 2024-03-24 162132](https://github.com/JisubShim/CV_Practice/assets/118372554/fb0c7a59-2c08-459b-a85b-f56213822cda)
(이미지의 egde를 잘못 detection한 것을 볼 수 있다.)

#### 한계
1. 색조 손실 : 엣지를 강조하여 카툰 스타일로 만드는 필터라, 원래 이미지의 색상과 색조를 완전히 보존하기 어렵다.
2. 세부 정보 손실 : median blur와 bilateral filter를 사용하며 노이즈를 제거하면서 이미지 특유의 텍스처같은 세부 정보들이 사라질 수 있다.
3. 매개변수 적용의 어려움 : Canny edge detector는 매개변수 값 최적화가 어렵기 때문에, 고정된 매개변수로 모든 이미지에 대해 일관된 결과를 기대하기 어렵다.

