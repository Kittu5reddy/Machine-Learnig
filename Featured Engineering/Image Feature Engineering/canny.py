import cv2
import matplotlib.pyplot as plt

image = cv2.imread('image_path')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, threshold1=100, threshold2=200)

plt.imshow(edges, cmap='gray')
plt.title('Canny Edge Detection')
plt.show()
