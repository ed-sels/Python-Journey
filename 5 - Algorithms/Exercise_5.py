def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

marks = []
print("Enter marks for 6 students:")
for i in range(6):
    mark = int(input(f"Student {i+1} mark: "))
    marks.append(mark)

print("Unsorted marks:", marks)
bubble_sort(marks)
print("Sorted marks:", marks)