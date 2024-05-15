import json
import sys
import time
import numpy as np
import cv2 as cv
from .line_drawing import draw_lines, set_line_drawing_settings
from ultralytics import YOLO

model = YOLO("models/cars.pt")

def load_settings(settings_file):
    try:
        with open('settings.json', 'r') as f:
            settings = json.load(f)
            return settings
    except FileNotFoundError:
        return None

def app(video_source):
    settings = load_settings('settings.json')
    if settings is None:
        print("Settings file not found! Loading default settings.")
        settings = {
            'line_spacing': .3,
            'line_length': .4,
            'width': 640,
            'height': 480,
            'recognized_items': {'cars': True, 'railings': True, 'poles': True, 'curbs': True},
        }
        
    set_line_drawing_settings(settings)    
    
    if video_source == 0:
        vid = cv.VideoCapture(0)
    elif video_source == 1:
        vid = cv.VideoCapture('../videos/video1.mp4')
    elif video_source == 2:
        vid = cv.VideoCapture('../videos/video2.mp4')
    else:
        print("Invalid video source.")
        exit()

    if not vid.isOpened():
        print("Failed to open video source")
        exit()

    fps = vid.get(cv.CAP_PROP_FPS)
    width, height = vid.get(cv.CAP_PROP_FRAME_WIDTH), vid.get(cv.CAP_PROP_FRAME_HEIGHT)

    need_resizing = width != settings['width'] or height != settings['height']

    while True:
        frame_processing_start = time.time()
        ret, frame = vid.read()
        if not ret:
            print("Can not receive frame")
            break

        if need_resizing:
            frame = cv.resize(frame, (settings['width'], settings['height']))

        results = model.track(frame, persist=True, conf=.60, verbose=False)
        
        frame = results[0].plot()

        frame = draw_lines(frame)

        cv.imshow('frame', frame)

        # for fixed fps
        time_now = time.time()
        while (time_now - frame_processing_start) < (1/fps):
            time_now = time.time()

        if cv.waitKey(int(1)) == ord('q'):
            break

    vid.release()

def main():
    if len(sys.argv) != 2 or sys.argv[1] not in ['0', '1', '2']:
        "Please specify a video source ID."
        exit(-1)
    else:
        app(int(sys.argv[1]))

if __name__ == '__main__':
    main()