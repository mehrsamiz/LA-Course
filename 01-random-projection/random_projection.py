import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.random_projection import johnson_lindenstrauss_min_dim, GaussianRandomProjection
from sklearn.metrics.pairwise import euclidean_distances

data = fetch_california_housing()
X = data.data  # Feature matrix
print(X[:2])

#JL Lemma
n_samples = X.shape[0]  
eps = 0.1  
min_dim = johnson_lindenstrauss_min_dim(n_samples=n_samples, eps=eps)
print(f"Minimum dimensions required for JL Lemma: {min_dim}")

#Gaussian Random Projection
transformer = GaussianRandomProjection(n_components=min_dim)
X_reduced = transformer.fit_transform(X)

#Compare Euclidean Distances
#Euclidean distances for original and reduced datasets
print(X_reduced[:2])
original_distances = euclidean_distances(X[:5], X[:5])  
reduced_distances = euclidean_distances(X_reduced[:5], X_reduced[:5]) 


print("Original distances (high-dimensional):")
print(original_distances)

print("\nReduced distances (low-dimensional):")
print(reduced_distances)



#epsilon
eps = np.arange(0.001, 0.999, 0.01)
colors = ['b', 'g', 'm', 'c']
m = [1e1, 1e3, 1e7, 1e10]
for i in range(4):
    min_dim = johnson_lindenstrauss_min_dim(n_samples=m[i], eps=eps)
    label = 'Total samples = ' + str(m[i])
    plt.plot(eps, np.log10(min_dim), c=colors[i], label=label)
    
plt.xlabel('eps')
plt.ylabel('log$_{10}$(d)')
plt.axhline(y=3.5, color='k', linestyle=':')
plt.legend()
plt.show()

