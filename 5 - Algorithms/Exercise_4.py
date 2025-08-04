def BinarySearch(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

print("Please enter a sorted list of 5 items:")
arr = []
for i in range(5):
    item = int(input(f"Enter item {i+1}: "))
    arr.append(item)

target = int(input("Please enter your target item:"))

result = BinarySearch(arr, target)
print(f"{target} found at index: {result}" if result != -1 else f"Not found")