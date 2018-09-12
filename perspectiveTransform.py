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

# pts1 = np.float32([[144,62], [1066, 92], [174, 979], [1041, 945]])
# change corners for each image you transform
pts1 = np.float32([[290,253], [1033,131], [36,896], [1257,907]])
pts2 = np.float32([[0,0], [1200, 0], [0, 1200], [1200, 1200]])

M = cv2.getPerspectiveTransform(pts1, pts2)

dst = cv2.warpPerspective(orig, M, (1200, 1200))

plt.imshow(dst)
plt.show()
