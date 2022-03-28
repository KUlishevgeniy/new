#### Написать алгоритм сортироки
#####
a = list(map(int, input().split()))

for i in range(len(a)):
    for j in range (i+1, len(a)):
        if a[i] > a[j]:
            c = a[i]
            a[i] = a[j]
            a[j] = c
print(a)
