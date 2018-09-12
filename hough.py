from picamera import PiCamera
import matplotlib.pyplot as plt
import numpy as np
import cv2

# read in image
filename = input('Input image filename to read:  ')
img = cv2.imread(filename)

# convert image from bgr to rgb
orig = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
print('Starting Image')
plt.imshow(orig)
plt.show()

# grayscale
gray = cv2.cvtColor(orig, cv2.COLOR_RGB2GRAY)
edges = cv2.Canny(gray, 50, 100, apertureSize=3)

# show starting image
print('Image after Canny')
plt.imshow(edges)
plt.show()

lines = cv2.HoughLines(edges, 1, np.pi/180, 125)
for line in lines:
    for r, theta in line:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * r
        y0 = b * r
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * a)
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * a)
        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

#show image after canny
print('Image after Hough')
plt.imshow(img)
plt.show()
