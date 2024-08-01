import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('path_to_your_image.jpg')
image_mat = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB

width, height, c = image_mat.shape

center = (width/2, height/2)


translate = np.float32([
    [1,0,50],
    [0,1,50]
])

scale = np.float32([
    [2,0,0],
    [0,2,0]
])

rotate = cv2.getRotatedMatrix2D(center,30,1)

translated_image = cv2.warpAffine(image_mat, translate, (width+50, height+50))
scaled_image = cv2.warpAffine(image_mat, scale, (width*2,height*2))
rotated_image = cv2.warpAffine(image_mat, rotate, (width, height))


# Plotting the images
fig, axes = plt.subplots(1, 4, figsize=(20, 5))

axes[0].imshow(image)
axes[0].set_title('Original Image')
axes[0].axis('off')

axes[1].imshow(translated_image)
axes[1].set_title('Translated Image')
axes[1].axis('off')

axes[2].imshow(rotated_image)
axes[2].set_title('Rotated Image')
axes[2].axis('off')

axes[3].imshow(scaled_image)
axes[3].set_title('Scaled Image')
axes[3].axis('off')

plt.show()
