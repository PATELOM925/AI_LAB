import numpy as np
import scipy as sc

arr = np.array([13,18,13,14,13,16,14,21,13])

mean = np.mean(arr)
print("The Mean is: ",mean)

median = np.median(arr)
print("The Median is: ",median)

mode = sc.stats.mode(arr)
print("The Mode is: ",mode[0])

data_range = np.ptp(arr)
print("The Range is: ",data_range)