import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

np.random.seed(0)
x =np.array([[2,10],[2,5],[8,4],[5,8],[7,5],[6,4],[1,2],[4,9]])
num_clusters = 3
kmeans = KMeans(n_clusters=num_clusters)
kmeans.fit(x)
cluster_centers = kmeans.cluster_centers_
labels = kmeans.labels_
print(cluster_centers)

plt.scatter(x[:,0],x[:,1],c=labels,cmap='viridis')
plt.scatter(cluster_centers[:, 0], cluster_centers[:, 1], marker='x', s=200, linewidths=3, color='r', label='Centroids')
plt.title('K-means Clustering')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()
