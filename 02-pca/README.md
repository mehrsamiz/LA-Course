# Principal Component Analysis (PCA)

This exercise applies **PCA** via SVD on the California Housing dataset to reduce dimensions and visualize variance explained.

##Output

Cumulative variance plot.

2D scatter plot of data in principal component space.

Comparison between original and reduced data.



Original Data Shape: (20640, 8)

![output plot](https://raw.githubusercontent.com/mehrsamiz/LA-Course/main/docs/pca2.png)


Reduced Data Shape: (20640, 2)

First 5 rows of the original data (non-standardized):
[[ 8.32520000e+00  4.10000000e+01  6.98412698e+00  1.02380952e+00
   3.22000000e+02  2.55555556e+00  3.78800000e+01 -1.22230000e+02]
 [ 8.30140000e+00  2.10000000e+01  6.23813708e+00  9.71880492e-01
   2.40100000e+03  2.10984183e+00  3.78600000e+01 -1.22220000e+02]
 [ 7.25740000e+00  5.20000000e+01  8.28813559e+00  1.07344633e+00
   4.96000000e+02  2.80225989e+00  3.78500000e+01 -1.22240000e+02]
 [ 5.64310000e+00  5.20000000e+01  5.81735160e+00  1.07305936e+00
   5.58000000e+02  2.54794521e+00  3.78500000e+01 -1.22250000e+02]
 [ 3.84620000e+00  5.20000000e+01  6.28185328e+00  1.08108108e+00
   5.65000000e+02  2.18146718e+00  3.78500000e+01 -1.22250000e+02]]

First 5 rows of the reduced data:
[[-1.88270434 -0.50336186]
 [-1.37111955 -0.12140565]
 [-2.08686762 -0.5011357 ]
 [-1.5758011  -1.23949529]
 [-1.59120582 -1.34526381]]


![output plot](https://raw.githubusercontent.com/mehrsamiz/LA-Course/main/docs/pca1.png)

##  Run
```bash
python pca.py
