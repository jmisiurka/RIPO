import time
import numpy as np
import cv2 as cv
from .line_drawing import draw_lines
from ultralytics import YOLO

model = YOLO("runs/detect/train4/weights/best.pt")

def main():
    vid = cv.VideoCapture('../videos/video1.mp4')
    # vid = cv.VideoCapture(0)
    if not vid.isOpened():
        print("Not opened")
        exit()

    fps = vid.get(cv.CAP_PROP_FPS)
    width, height = vid.get(cv.CAP_PROP_FRAME_WIDTH) * 2, vid.get(cv.CAP_PROP_FRAME_HEIGHT) * 2

    while True:
        frame_processing_start = time.time()
        ret, frame = vid.read()

        result = model(frame, stream=True)

        frame = cv.resize(frame, None, frame, 2, 2)

        if not ret:
            print("Can not receive frame")
            break

        frame = draw_lines(frame, width, height)

        cv.imshow('frame', frame)

        # for fixed fps
        time_now = time.time()
        while (time_now - frame_processing_start) < (1/fps):
            time_now = time.time()

        if cv.waitKey(int(1)) == ord('q'):
            break

    vid.release()

if __name__ == '__main__':
    main()