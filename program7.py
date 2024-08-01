import cv2
import matplotlib.pyplot as plt

img = cv2.imread('fruit.png')
img_mat = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

width, height, channel = img_mat.shape

midx = width//2
midy = height//2

images = [image_mat[:midy,:midx], image_mat[:midy, midx:], iamge_mat[midy:, :midx], image_mat[midy:, midx:]]
titles = ["top left","top right","bottom left","bottom right"]

fig, axs = plt.subplot(2,2,figsize=(10,10))

for i in range(2):
    for j in range(2):
        axs[i, j].imshow(images[i*2 + j])
        axs[i, j].set_title(titles[i*2 + j])
        axs[i, j].axis("off")
plt.show()
