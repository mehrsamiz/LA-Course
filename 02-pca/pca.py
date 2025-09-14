import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import fetch_california_housing


data = fetch_california_housing()
X = data.data
print("Original Data Shape:", X.shape) 


scaler = StandardScaler()
X_std = scaler.fit_transform(X)

U, S, Vt = np.linalg.svd(X_std, full_matrices=False)


n_samples = X_std.shape[0]
explained_variance = (S**2) / (n_samples - 1)  # Variance for each singular value
explained_variance_ratio = explained_variance / np.sum(explained_variance)  # Normalized ratio
cumulative_variance = np.cumsum(explained_variance_ratio)

# Plot cumulative variance
plt.figure(figsize=(10, 6))
plt.plot(range(1, len(cumulative_variance) + 1), cumulative_variance, marker='o', color='b')
plt.title('Cumulative Variance Explained by Principal Components')
plt.xlabel('Number of Principal Components')
plt.ylabel('Cumulative Variance Ratio')
plt.grid()
plt.show()


V_2 = Vt.T[:, :2]  
X_reduced = np.dot(X_std, V_2)
print("Reduced Data Shape:", X_reduced.shape)


print("\nFirst 5 rows of the original data (non-standardized):")
print(X[:5])  # Original data (non-standardized)
print("\nFirst 5 rows of the reduced data:")
print(X_reduced[:5])  # Reduced data

plt.scatter(X_reduced[:, 0], X_reduced[:, 1], alpha=0.5)
plt.title('2D Representation after PCA')
plt.xlabel('First Principal Component')
plt.ylabel('Second Principal Component')
plt.grid(True)
plt.show()
