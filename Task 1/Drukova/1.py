#### Написать алгоритм сортироки
#####

def bubble_sort(arr):
    for i in range(0, len(arr) - 1):
        for j in range(len(arr) - 1):
            if (arr[j] > arr[j + 1]):
                t = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = t
    return arr

arr = input('Enter the list of numbers: ').split()
print(bubble_sort(arr))