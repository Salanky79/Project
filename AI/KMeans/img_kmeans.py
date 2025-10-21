import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
img = plt.imread(r"d:\sonlailaptrinh\AI\KMeans\a.jpg")

height = img.shape[0]
width = img.shape[1]
channel = img.shape[2]

# print(img.shape)
# (   ,   ,   ) tuple - read only

img = img.reshape(height*width, channel)  # duỗi ảnh thẳng ra

kmeans = KMeans(n_clusters=3).fit(img)
labels = kmeans.predict(img)
clusters = kmeans.cluster_centers_


img2 = np.zeros_like(img)  # numpy tự biến đổi

for i in range(len(img2)):
    img2[i] = clusters[labels[i]]

img2 = img2.reshape(height, width, channel)


plt.imshow(img2)
plt.show()
