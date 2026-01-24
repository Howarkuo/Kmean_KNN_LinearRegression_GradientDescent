import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy
import cv2

#image segmentation
# read image by matplotlib
# Kmeans package to divide pixels in 5 color cluster and print 
# output:
# ## labels
# (368016 ,3) = 368,016 individual data points,$612 \times 601$ or $700 \times 525$ pixels.
#  (3): This represents the RGB channels (Red, Green, Blue).
# ## clusters
# [[128.77875015 139.28019367  93.40881751]
#  [112.42167859 125.64036335  37.92039044]
#  [204.51169063 209.84822862 210.41162941]
#  [ 84.12581329 117.81031905 173.67918108]
#  [ 47.39032796  55.99563311  27.40590144]]
# Cluster,Red,Green,Blue,Estimated Color
# 0,128.7,139.2,93.4,Muted Olive/Green
# 1,112.4,125.6,37.9,Darker Earthy Green
# 2,204.5,209.8,210.4,Off-White/Grey
# 3,84.1,117.8,173.6,Soft Blue
# 4,47.3,55.9,27.4,Very Dark Brown/Green

img = plt.imread("fig/a.jpg")

width = img.shape[0]
height = img.shape[1]

img = img.reshape(width*height,3)

print(img.shape)

kmeans = KMeans(n_clusters=5).fit(img)

labels = kmeans.predict(img)
clusters = kmeans.cluster_centers_

print(labels)
print(clusters)

#create the new image with same shape and data type as the original img
# all value are 0

# for loop: O(N-368016)
# img2 = numpy.zeros_like(img)

# #loop throught each pixel
# for i in range(len(img2)):
# 	img2[i] = clusters[labels[i]]

# rewrite 
img2 =clusters[labels].astype(img.dtype)

#reshape new 2 d image
img2 = img2.reshape(width,height,3)
# display image
plt.imshow(img2)
plt.show()


img3 = clusters[labels].reshape(width, height, 3).astype(numpy.uint8)

plt.imshow(img3)
plt.show()

# gray image
gray = img3.mean(axis=2).astype(numpy.uint8)

plt.imshow(gray, cmap="gray")
plt.show()

# rotation 90 degree
rot90 = numpy.rot90(img3)
plt.imshow(rot90)
plt.show()

# rotation 180 degree
rot180 = numpy.rot90(img3, 2)
plt.imshow(rot180)
plt.show()


(h, w) = img3.shape[:2]
M = cv2.getRotationMatrix2D((w//2, h//2), 45, 1.0)

rot = cv2.warpAffine(img3, M, (w, h))

plt.imshow(rot)
plt.show()



# Sort clusters to make the palette look organized (optional)
palette = clusters.astype(numpy.uint8)
palette = palette[numpy.argsort(palette.sum(axis=1))] # Sort by brightness

# Create a blank canvas for the palette (50px high, 300px wide)
bar = numpy.zeros((50, 300, 3), dtype="uint8")
step = 300 // 5

for i in range(5):
    bar[:, i*step:(i+1)*step] = palette[i]

plt.figure(figsize=(8, 2))
plt.title("Dominant Colors (K-Means)")
plt.imshow(bar)
plt.axis('off')
plt.show()