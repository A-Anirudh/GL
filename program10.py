img = cv.imread('messi.jpeg')
img_rgb = img[:,:,::-1]
avgBlur = cv.blur(img_rgb,(5,5))
gaussianBlur=cv.GaussianBlur(img_rgb,(5,5),0)
medianBlur = cv.medianBlur(img_rgb, 5)
bilateralFilter = cv.bilateralFilter(img_rgb, 9, 75, 75)
boxFilter = cv.boxFilter(img_rgb, -1, (5, 5))  # Box Filter for smoothing
images = [img_rgb, avgBlur, gaussianBlur, medianBlur, bilateralFilter, boxFilter]
titles = ['Original', 'Average Blur', 'Gaussian Blur', 'Median Blur', 'Bilateral Filter', 'Box Filter']
plt.figure(figsize=(12, 8))
for i in range(len(images)):
    plt.subplot(2, 3, i + 1)
    plt.title(titles[i])
    plt.imshow(images[i])
    plt.axis('off')  # Hide axes

plt.tight_layout()
plt.show()


#### Both above and below work

import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.metrics import structural_similarity as ssim

# Load the image
image = cv2.imread('fruit.jpg')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Define the kernel size
kernel_size = 9

# Define the blur kernel
blur_kernel = np.ones((kernel_size, kernel_size), dtype=np.float32) / (kernel_size * kernel_size)

# Apply the blur filter
blurred = cv2.filter2D(image_rgb, -1, blur_kernel)

# Define the smooth kernel
smooth_kernel = np.array([[2, 2, 2],
                          [2, 10, 2],
                          [2, 2, 2]], dtype=np.float32) / 18

# Apply the smooth filter
smoothed = cv2.filter2D(image_rgb, -1, smooth_kernel)

# Convert images to grayscale for SSIM comparison
gray_original = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2GRAY)
gray_blurred = cv2.cvtColor(blurred, cv2.COLOR_RGB2GRAY)
gray_smoothed = cv2.cvtColor(smoothed, cv2.COLOR_RGB2GRAY)

# Compute SSIM between original and blurred/smoothed images
ssim_original_blurred, _ = ssim(gray_original, gray_blurred, full=True)
ssim_original_smoothed, _ = ssim(gray_original, gray_smoothed, full=True)

# Print the SSIM values
print(f'SSIM between original and blurred images: {ssim_original_blurred:.4f}')
print(f'SSIM between original and smoothed images: {ssim_original_smoothed:.4f}')

# Plotting the images
fig, axs = plt.subplots(1, 3, figsize=(18, 6))

axs[0].imshow(image_rgb)
axs[0].set_title('Original Image')
axs[0].axis('off')

axs[1].imshow(blurred)
axs[1].set_title('Blurred Image')
axs[1].axis('off')

axs[2].imshow(smoothed)
axs[2].set_title('Smoothed Image')
axs[2].axis('off')

plt.tight_layout()
plt.show()
