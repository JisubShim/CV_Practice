# CV_calibration_&_distortion_correction
OpenCV를 통해 vedio를 calibration한 다음 distortion correction 해보았습니다.

#### 카메라 캘리브레이션 기능
video를 재생 중에 Space를 누르면 정지하고 격자점을 표시합니다. 그 다음 Enter를 누르면 다시 재생되고 프레임이 저장된다. 이렇게 반복할 때마다 NSelect(The number of selected images)가 1씩 증가한다. <br>
![스크린샷 2024-04-01 020150](https://github.com/JisubShim/CV_Practice/assets/118372554/22ba53b0-d1e4-4ede-ac16-bd4e0167bee4)
<br>
<br>
그렇게 video가 끝나거나 ESC를 누르면 종료되며 콘솔창에 calibration 결과값(The number of selected images, RMS Error, Camera Matrix, Distortion coefficient)을 출력한다.
<br>
![스크린샷 2024-04-01 020245](https://github.com/JisubShim/CV_Practice/assets/118372554/74b9efb5-4e01-4d45-881c-c0df4af0eb6b)

#### 렌즈 왜곡 보정 기능
cv.remap을 이용하여 렌즈 왜곡을 보정하였습니다. <br>
Tab으로 보정 전, 후를 전환할 수 있습니다.
<br>
**보정 전**
<br>
![스크린샷 2024-04-01 020023](https://github.com/JisubShim/CV_Practice/assets/118372554/55feea41-c220-4c6c-bd63-ce46729902cb)
<br>
<br>
**보정 후**
<br>
![스크린샷 2024-04-01 020045](https://github.com/JisubShim/CV_Practice/assets/118372554/d13761e1-a6c9-4b59-8acb-750d14452acf)


- vedio는 전에 만든 CV_video_recorder로 촬영하였습니다.