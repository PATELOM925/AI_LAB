#find mean of 13,18,13,14,13,16,14,21,13
def mean(arr):
    i = 0
    sum = 0
    for arr[i] in arr:
        sum = arr[i] + sum
        mean = sum/len(arr)
    return mean    
        
        

arr  = [13,18,13,14,13,16,14,21,13]
avg = mean(arr)      
print("The average is",avg)      