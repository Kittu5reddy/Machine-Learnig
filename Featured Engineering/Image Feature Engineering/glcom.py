import numpy as np
import skimage.feature as feature

image = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])  # Example image
glcm = feature.greycomatrix(image, distances=[1], angles=[0], symmetric=True, normed=True)
contrast = feature.greycoprops(glcm, prop='contrast')
print('GLCM Contrast:', contrast)
