import cv2
import numpy as np

import matplotlib.pyplot as plt

image = cv2.imread('image.png')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image_mat = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

sobel_x = np.array([[-1,0,1],
                    [-2,0,2],
                    [-1,0,1]
                   ])
sobel_y = np.array([
  [-1,-2,-1],
  [0,0,0],
  [1,2,1]
])


edges_x = cv2.filter2D(gray_image, -1, sobel_x)
edges_y = cv2.filter2D(gray_image, -1, sobel_y)

edges = cv2.addWeighted(edges_x,0.5, edges_y,0.5, 0)

titles = ["Original", "edge X","edge y", "combined"]
array = [image_mat, edges_x, edges_y, edges]

fig, axs = plt.subplot(1,4, figsize=(150,150))
for i in range(4):
  axs[i].imshow(array[i])
  axs[i].set_title(titles[i])

plt.show()
sobel_x = cv2.Sobel(gray_image, cv2.CV_64F,1,0,ksize=5)
sobel_y= cv2.Sobel(gray_image, cv2.CV_64F,0,1,ksize=5)

texture = sobel_x + sobel_y

newTitle = ["Original", "Edge Detection", "Texture"]
newArr = [image_mat, edges, texture]

fig,axs = plt.subplot(1,3, figsize=(150,150))
for i in range(2):
  axs[i].imshow(newArr[i])
  axs[i].set_title(newTitle[i])

plt.show()
