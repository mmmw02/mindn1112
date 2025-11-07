import cv2
import numpy as np


img_files = ['1.jpg', '2.jpg', '3.jpg', '4.jpg']

def yellow_mask_as_white(img_path):
    img = cv2.imread(img_path)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_yellow = np.array([0, 170, 170])
    upper_yellow = np.array([90, 255, 255])
    mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask_yellow, cv2.MORPH_CLOSE, kernel)
    result = np.zeros_like(img)
    result[mask != 0] = [255, 255, 255]
    return result

for idx, img_file in enumerate(img_files):
    out_img = yellow_mask_as_white(img_file)
    cv2.imwrite(f'out_yellow_{idx+1}.png', out_img)