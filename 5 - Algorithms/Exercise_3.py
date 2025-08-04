def Linear_Search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr , target = [1, 2, 3, 4, 5], 4
result = Linear_Search(arr, target)
print(f"{target} found at index: {result}" if result != -1 else f"{target} not found in the array")