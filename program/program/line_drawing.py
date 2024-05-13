import numpy as np
import cv2 as cv

line_width_factor = .3
line_height_factor = .95
# convergence = 0.5

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

def draw_lines(frame, width, height):
    overlay = np.copy(frame)

    cv.line(overlay, (int(width * line_width_factor), int(height)), (int(width * line_width_factor), int(height * line_height_factor)), (0, 0, 255), 5)
    cv.line(overlay, (int(width - width * (line_width_factor)), int(height)), (int(width - width * line_width_factor), int(height * line_height_factor)), (0, 0, 255), 5)

    cv.line(overlay, (int(width * line_width_factor), int(height * line_height_factor)), (int(width * line_width_factor), int(height * line_height_factor ** 2)), (0, 255, 255), 5)
    cv.line(overlay, (int(width - width * (line_width_factor)), int(height * line_height_factor)), (int(width - width * line_width_factor), int(height * line_height_factor ** 2)), (0, 255, 255), 5)

    cv.line(overlay, (int(width * line_width_factor), int(height * line_height_factor ** 2)), (int(width * line_width_factor), int(height * line_height_factor ** 3)), (0, 255, 0), 5)
    cv.line(overlay, (int(width - width * (line_width_factor)), int(height * line_height_factor ** 2)), (int(width - width * line_width_factor), int(height * line_height_factor ** 3)), (0, 255, 0), 5)

    frame = cv.addWeighted(frame, 0, overlay, 1, 0)
    return frame