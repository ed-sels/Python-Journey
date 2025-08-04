import numpy as np

arr = np.arange(10, 51)

print("Array:", arr)
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Median:", np.median(arr))
print("Squares:", arr ** 2)
print("Even numbers:", arr[arr % 2 == 0])