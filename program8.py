import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load and convert the image from BGR to RGB
image = cv2.imread('path_to_your_image.jpg')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Get image dimensions
height, width, _ = image_rgb.shape

# Define transformations
translate_matrix = np.float32([[1, 0, 50], [0, 1, 50]])  # Translate by (50, 50)
scale_matrix = np.float32([[2, 0, 0], [0, 2, 0]])        # Scale by 2x
rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), 30, 1)  # Rotate by 30 degrees

# Apply transformations
translated_image = cv2.warpAffine(image_rgb, translate_matrix, (width + 50, height + 50))
scaled_image = cv2.warpAffine(image_rgb, scale_matrix, (width * 2, height * 2))
rotated_image = cv2.warpAffine(image_rgb, rotation_matrix, (width, height))

# Plot images
fig, axes = plt.subplots(1, 4, figsize=(20, 5))

# Display images
axes[0].imshow(image_rgb)
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
