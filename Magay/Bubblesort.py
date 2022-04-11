def sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [84, 34, 25, 12, 22, 21, 91]
sort(arr)
print ("Сортированный массив:")
for i in range(len(arr)):
    print ("%d" %arr[i])
