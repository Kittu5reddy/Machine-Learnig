from skimage.feature import hog
from skimage import data, exposure
import matplotlib.pyplot as plt
image = data.astronaut()  # Sample image
fd, hog_image = hog(image, pixels_per_cell=(16, 16), cells_per_block=(1, 1), visualize=True)

hog_image_rescaled = exposure.rescale_intensity(hog_image, in_range=(0, 10))
plt.imshow(hog_image_rescaled, cmap=plt.cm.gray)
plt.title('Histogram of Oriented Gradients (HOG)')
plt.show()
