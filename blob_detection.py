import cv2
import numpy as np

img = cv2.imread(input("Image file name: "), cv2.IMREAD_GRAYSCALE)

params = cv2.SimpleBlobDetector_Params()

params.minThreshold = 10
params.maxThreshold = 200

params.minArea = 50
params.maxArea = 20000

params.filterByCircularity = True
params.minCircularity = 0.1

params.filterByConvexity = True
params.minConvexity = 0.87

params.filterByInertia = True
params.minInertiaRatio = 0.01

def filter_by_color():
    params.filterByColor = True
    params.filterByArea = False
    blobColor = 0

def filter_by_size():
    params.filterByColor = False
    params.filterByArea = True

def get_img():
    detector = cv2.SimpleBlobDetector_create(params)

    keypoints = detector.detect(img)

    return cv2.drawKeypoints(img, keypoints, np.array([]), (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

option = input("1: Filter by Color\nElse: Filter by size\n")

def choose_filter_option():
    if(int(option) == 1):
        filter_by_color
    else:
        filter_by_size()

choose_filter_option()

cv2.imshow("Blobs detected by size", get_img())
cv2.waitKey(0)
cv2.destroyAllWindows()
