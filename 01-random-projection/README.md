# Random Projection & Johnson–Lindenstrauss Lemma

This exercise demonstrates dimensionality reduction using **Johnson–Lindenstrauss Lemma** and **Gaussian Random Projection** on the California Housing dataset.

##  Output


Prints minimum dimensions required for JL Lemma.

Compares Euclidean distances in original vs reduced space.

Plots the relationship between eps and required dimensions.


[[ 8.32520000e+00  4.10000000e+01  6.98412698e+00  1.02380952e+00
   3.22000000e+02  2.55555556e+00  3.78800000e+01 -1.22230000e+02]
 [ 8.30140000e+00  2.10000000e+01  6.23813708e+00  9.71880492e-01
   2.40100000e+03  2.10984183e+00  3.78600000e+01 -1.22220000e+02]]
Minimum dimensions required for JL Lemma: 8515
[[  0.65474724  -1.51291461   4.16821353 ...   2.35814104   4.94979424
    6.51446448]
 [  5.44596851 -16.05626706  16.77441764 ...  20.4693409   27.33598023
   42.31540563]]
Original distances (high-dimensional):
[[   0.         2079.09638038  174.3556852   236.27432956  243.29138734]
 [2079.09638038    0.         1905.25373184 1843.26271779 1836.2671017 ]
 [ 174.3556852  1905.25373184    0.           62.07072993   69.11618476]
 [ 236.27432956 1843.26271779   62.07072993    0.            7.25113659]
 [ 243.29138734 1836.2671017    69.11618476    7.25113659    0.        ]]

Reduced distances (low-dimensional):
[[2.01854806e-05 2.08298019e+03 1.74676129e+02 2.36699960e+02
  2.43715773e+02]
 [2.08298019e+03 0.00000000e+00 1.90881183e+03 1.84671655e+03
  1.83972060e+03]
 [1.74676129e+02 1.90881183e+03 0.00000000e+00 6.21744686e+01
  6.92187943e+01]
 [2.36699960e+02 1.84671655e+03 6.21744686e+01 3.89024316e-05
  7.24973914e+00]
 [2.43715773e+02 1.83972060e+03 6.92187943e+01 7.24973914e+00
  0.00000000e+00]]

![output plot](https://raw.githubusercontent.com/mehrsamiz/LA-Course/main/docs/random_proj.png)

## 🚀 Run
```bash
python random_projection.py
