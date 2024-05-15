import numpy as np
import cv2 as cv
import json

line_spacing = .3
line_length = .4
width = 640
height = 480

total_length = line_length * height
total_spacing = line_spacing * width

def set_line_drawing_settings(settings):
    global line_spacing, line_length, width, height, total_length, total_spacing
    
    line_spacing = settings['line_spacing']
    line_length = settings['line_length']
    width = settings['width']
    height = settings['height']
    total_length = line_length * height
    total_spacing = line_spacing * width

# def apply_distortion(frame):
    # map_x, map_y = np.meshgrid(np.arange(width), np.arange(height))
    # x_normalized = (2 * map_x - width) / width
    # y_normalized = (2 * map_y - height) / height

    # r_squared = x_normalized**2 + y_normalized**2
    # r_distorted = 1 + 1 * r_squared + 1 * r_squared**2

    # x_distorted = x_normalized * r_distorted
    # y_distorted = y_normalized * r_distorted + map_y - height

    # x_mapped = ((x_distorted + 1) * width) / 2
    # y_mapped = ((y_distorted + 1) * height) * .9

    # frame = cv.remap(frame_copy, x_mapped.astype(np.float32), y_mapped.astype(np.float32), interpolation=cv.INTER_LINEAR)

    # cv.remap(frame, )

def draw_lines_with_settings(frame, settings):
    line_spacing = 1 - settings['line_spacing']
    line_length = settings['line_length']
    width = settings['width']
    height = settings['height']

    total_length = line_length * height
    total_spacing = line_spacing * width

    cv.line(frame, (int(.5 * total_spacing), int(height)), (int(.5 * total_spacing), int(height - total_length / 3)), (0, 0, 255), 5)
    cv.line(frame, (int(width - .5 * total_spacing), int(height)), (int(width - .5 * total_spacing), int(height - total_length / 3)), (0, 0, 255), 5)

    cv.line(frame, (int(.5 * width * line_spacing), int(height - total_length / 3)), (int(.5 * width * line_spacing), int(height - total_length * 2 / 3)), (0, 255, 255), 5)
    cv.line(frame, (int(width - .5 * total_spacing), int(height - total_length / 3)), (int(width - .5 * total_spacing), int(height - total_length * 2 / 3)), (0, 255, 255), 5)

    cv.line(frame, (int(.5 * width * line_spacing), int(height - total_length * 2 / 3)), (int(.5 * width * line_spacing), int(height - total_length)), (0, 255, 0), 5)
    cv.line(frame, (int(width - .5 * total_spacing), int(height - total_length * 2 / 3)), (int(width - .5 * total_spacing), int(height - total_length)), (0, 255, 0), 5)

    return frame

def draw_lines(frame):
    
    
    cv.line(frame, (int(.5 * total_spacing), int(height)), (int(.5 * total_spacing), int(height - total_length / 3)), (0, 0, 255), 5)
    cv.line(frame, (int(width - .5 * total_spacing), int(height)), (int(width - .5 * total_spacing), int(height - total_length / 3)), (0, 0, 255), 5)

    cv.line(frame, (int(.5 * width * line_spacing), int(height - total_length / 3)), (int(.5 * width * line_spacing), int(height - total_length * 2 / 3)), (0, 255, 255), 5)
    cv.line(frame, (int(width - .5 * total_spacing), int(height - total_length / 3)), (int(width - .5 * total_spacing), int(height - total_length * 2 / 3)), (0, 255, 255), 5)

    cv.line(frame, (int(.5 * width * line_spacing), int(height - total_length * 2 / 3)), (int(.5 * width * line_spacing), int(height - total_length)), (0, 255, 0), 5)
    cv.line(frame, (int(width - .5 * total_spacing), int(height - total_length * 2 / 3)), (int(width - .5 * total_spacing), int(height - total_length)), (0, 255, 0), 5)

    return frame