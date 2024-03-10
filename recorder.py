import cv2 as cv
import tkinter as tk
import numpy as np
from tkinter import filedialog
from tkinter import messagebox  # 추가

class VideoRecorder:
    def __init__(self):
        self.cap = cv.VideoCapture(0)  # 인자값 0으로 설정. 디폴트 카메라
        self.record_mode = False
        self.out = None
        self.contrast = 1.0
        self.brightness = 0.0
        self.flip = False
        self.show_help = False
        self.output_filename = None

        # 카메라 크기 확인
        if not self.cap.isOpened():
            print("Error: Could not open camera.")
            exit()

    def start_recording(self, filename=None, fourcc=cv.VideoWriter_fourcc(*'XVID'), fps=20.0):
        if filename is not None:
            self.output_filename = filename
        else:
            # 사용자에게 녹화할 파일명을 입력하도록 요청
            self.output_filename = filedialog.asksaveasfilename(defaultextension=".avi",
                                                                filetypes=[("AVI file", "*.avi"), ("MP4 file", "*.mp4")],
                                                                title="Save")
        if not self.output_filename:
            # 사용자가 파일명 입력을 취소한 경우
            self.record_mode = not self.record_mode
            return

        self.out = cv.VideoWriter(self.output_filename, fourcc, fps, (640, 480))

    def stop_recording(self):
        if self.out is not None:
            self.out.release()

    def ask_overwrite_confirmation(self, file_path):
        # 파일 덮어쓰기 여부 확인 창
        root = tk.Tk()
        root.withdraw()
        response = messagebox.askokcancel("경고", f"파일 '{file_path.name}'가 이미 존재합니다. 덮어쓰시겠습니까?")
        return response

    def apply_filter(self, img):
        # Contrast 및 Brightness 조정
        # img = cv.convertScaleAbs(img, alpha=self.contrast, beta=self.brightness)
        img = self.contrast * img + self.brightness
        # overflow 방지
        img[img < 0] = 0 
        img[img > 255] = 255
        img = img.astype(np.uint8)

        # Flip 적용
        if self.flip:
            img = cv.flip(img, 1)

        return img

    def display_help(self, img):
        # 도움말 표시
        help_text = "Recording : 'Space bar' | Adjust Contrast : 'c'/'C' | Adjust Brightness : 'b'/'B' | Flip : 'f' | Exit : 'ESC'"
        cv.putText(img, help_text, (10, 460), cv.FONT_HERSHEY_SIMPLEX, 0.36, (255, 255, 255), 1, cv.LINE_AA)

    def run(self):
        while True:
            ret, img = self.cap.read()

            if not ret:
                print("Error: Failed to read img.")
                break

            # 필터 적용
            img = self.apply_filter(img)

            # help HUD 표시
            self.display_help(img)

            # 녹화 중일 때 빨간색 원 표시
            if self.record_mode:
                cv.circle(img, (50, 50), 30, (0, 0, 255), -1)

            # 녹화 중이 아닐 때만 Help 표시
            if not self.record_mode and self.show_help:
                self.display_help(img)

            # 녹화
            if self.record_mode:
                self.out.write(img)

            # 화면에 현재 카메라 영상 표시
            cv.imshow('Video Recorder', img)

            key = cv.waitKey(1) # 프레임 0.001s
            if key == ord(' '): # ord() : 하나의 문자를 인자로 받고 해당 문자의 유니코드 정수 반환
                # Space 키로 Record 모드 토글
                self.record_mode = not self.record_mode
                if(self.record_mode == True):
                    recorder.start_recording()  # 녹화 전 파일명 입력
            elif key == ord('c'):
                # 'c' 키로 Contrast 값을 증가
                self.contrast += 0.1
            elif key == ord('C'):
                # 'C' 키로 Contrast 값을 감소
                self.contrast -= 0.1
            elif key == ord('b'):
                # 'b' 키로 Brightness 값을 증가
                self.brightness += 1
            elif key == ord('B'):
                # 'B' 키로 Brightness 값을 감소
                self.brightness -= 1
            elif key == ord('f'):
                # 'f' 키로 Flip 값을 토글
                self.flip = not self.flip
            elif key == ord('H'):
                # 'H' 키로 Help 표시 여부 토글
                self.show_help = not self.show_help
            elif key == 27:  # ESC 키로 종료
                self.stop_recording()
                break

        self.cap.release()
        cv.destroyAllWindows()

if __name__ == "__main__":
    recorder = VideoRecorder()
    recorder.run()
