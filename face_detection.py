import cv2
import matplotlib.pyplot as plt

# Load the image
image_path = 'cricket.jpg'
image = cv2.imread(image_path)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +
'haarcascade_frontalface_default.xml')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Detect faces in the image
faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5,
minSize=(30, 30))
# Initialize a list to store cropped faces
cropped_faces = []
# Draw rectangles around the detected faces and crop them
for (x, y, w, h) in faces:
  cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
  cropped_faces.append(image[y:y+h, x:x+w])
# Display each cropped face separately
plt.figure(figsize=(12, 6))
for i, face in enumerate(cropped_faces):
plt.subplot(1, len(cropped_faces), i + 1)
plt.imshow(cv2.cvtColor(face, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.title(f'Face {i + 1}')
plt.tight_layout()
plt.show()
