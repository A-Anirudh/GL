import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('path_to_your_image.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB

# Function to translate the image
def translate(image, tx, ty):
    rows, cols, _ = image.shape
    M = np.float32([[1, 0, tx], [0, 1, ty]])
    translated_image = cv2.warpAffine(image, M, (cols, rows))
    return translated_image

# Function to rotate the image
def rotate(image, angle):
    rows, cols, _ = image.shape
    M = cv2.getRotationMatrix2D((cols/2, rows/2), angle, 1)
    rotated_image = cv2.warpAffine(image, M, (cols, rows))
    return rotated_image

# Function to scale the image
def scale(image, fx, fy):
    scaled_image = cv2.resize(image, None, fx=fx, fy=fy, interpolation=cv2.INTER_LINEAR)
    return scaled_image

# Translate, rotate, and scale the image
translated_image = translate(image, 50, 50)
rotated_image = rotate(image, 45)
scaled_image = scale(image, 0.5, 0.5)

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
