import numpy as np
import cv2 as cv

# 주어진 동영상 및 캘리브레이션 데이터
video_file = 'chessboard.avi'
K = np.array([[623.52090757, 0, 350.78233483],
              [0, 624.37909215, 258.33046718],
              [0, 0, 1]])
dist_coeff = np.array([-4.12822673e-01, -6.14835325e-02, -3.08760254e-04, -4.01559378e-03, 7.11213308e-01])
board_pattern = (10, 7)
board_cellsize = 0.025
board_criteria = cv.CALIB_CB_ADAPTIVE_THRESH + cv.CALIB_CB_NORMALIZE_IMAGE + cv.CALIB_CB_FAST_CHECK

# 동영상 열기
video = cv.VideoCapture(video_file)
assert video.isOpened(), '입력을 읽을 수 없습니다. ' + video_file

# 직사각형 준비
rect_lower_left = board_cellsize * np.array([4, 2, 0])
rect_upper_right = board_cellsize * np.array([5, 4, 0])

# 카메라를 보정하기 위한 3D 포인트 준비
obj_points = board_cellsize * np.array([[c, r, 0] for r in range(board_pattern[1]) for c in range(board_pattern[0])])

# 포즈 추정 실행
while True:
    # 동영상에서 이미지 읽기
    valid, img = video.read()
    if not valid:
        break

    # 카메라 자세 추정
    success, img_points = cv.findChessboardCorners(img, board_pattern, board_criteria)
    if success:
        ret, rvec, tvec = cv.solvePnP(obj_points, img_points, K, dist_coeff)

        # 이미지에 직사각형 그리기
        rect_points = np.array([rect_lower_left, [rect_upper_right[0], rect_lower_left[1], 0], rect_upper_right, [rect_lower_left[0], rect_upper_right[1], 0]])
        rect_points_2d, _ = cv.projectPoints(rect_points, rvec, tvec, K, dist_coeff)
        rect_points_2d = np.int32(rect_points_2d).reshape(-1, 2)
        cv.polylines(img, [rect_points_2d], True, (255, 0, 0), 2)

        # 카메라 위치 출력
        R, _ = cv.Rodrigues(rvec)
        p = (-R.T @ tvec).flatten()
        info = f'XYZ: [{p[0]:.3f} {p[1]:.3f} {p[2]:.3f}]'
        cv.putText(img, info, (10, 25), cv.FONT_HERSHEY_DUPLEX, 0.6, (0, 255, 0))

    # 이미지 표시 및 키 이벤트 처리
    cv.imshow('Pose Estimation (Chessboard)', img)
    key = cv.waitKey(10)
    if key == ord(' '):
        key = cv.waitKey()
    if key == 27: # ESC
        break

video.release()
cv.destroyAllWindows()
