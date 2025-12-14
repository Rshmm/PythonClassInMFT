arr = [5, 2, 9, 1, 5, 6,56,78,436,25,0]
n = len(arr)
print(len(arr))

for i in range(n-1):
    for j in range(0, n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print(arr)
