
def mode(arr):
    freq = {}
    for item in arr:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1

    max_frequency = max(freq.values())
    mode = [key for key, value in freq.items() if value == max_frequency]
    return mode

arr  = [13,18,13,14,13,16,14,21,13]
result = mode(arr)
print("Mode(s):", result)
