import cv2
import numpy as np

file_name = "in.jpg"

img = cv2.imread(file_name)
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

height, width, _ = img.shape
pixels = height * width

colors, counts = np.unique(hsv_img.reshape(-1, 3), axis = 0, return_counts=True)

for color, count in zip(colors, counts):
    if(count > 0.01 * width):
        lower, upper = color * 0.99, color * 1.01
        mask = cv2.inRange(img, lower, upper)
        masked_img = cv2.bitwise_and(hsv_img, hsv_img, mask=mask)
        cv2.imshow("Image Window", masked_img)
    else:
        continue