import time

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min = i
        for j in range(i+1, n):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]

numbers = [23, 5, 12, 7, 34, 2, 19, 45, 8, 27]  # Predefined list

# Selection sort performance
unsorted1 = numbers.copy()
start_sel = time.time()
selection_sort(unsorted1)
end_sel = time.time()

# Built-in sorted() performance
unsorted2 = numbers.copy()
start_builtin = time.time()
sorted_builtin = sorted(unsorted2)
end_builtin = time.time()

print("Selection Sort result:", unsorted1)
print(f"Selection Sort time: {end_sel - start_sel:.6f} seconds")
print("Built-in sorted() result:", sorted_builtin)
print(f"Built-in sorted() time: {end_builtin - start_builtin:.6f} seconds")
print("Selection Sort is faster than built-in sorted()" if (end_sel - 
    start_sel) < (end_builtin - start_builtin) else "Built-in sorted() is faster than Selection Sort")