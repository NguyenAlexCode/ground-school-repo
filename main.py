import cv2

filename = "in.jpg"

img = cv2.imread(filename)

img[:,:,1] = 0

img = cv2.resize(img, (1000, 300))

cv2.imwrite("out.jpg", img)
