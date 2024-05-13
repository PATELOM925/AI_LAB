arr  = [13,18,13,14,13,16,14,21,13]
 
def median(arr):
    arr.sort()
    length = len(arr)
    if length % 2 == 0:
        median1 = arr[length//2]
        median2 = arr[length//2 - 1]
        median = (median1 + median2)/2
    else:
        median = arr[length//2]
    return median

med = median(arr)   
print("the median is",med)     
    