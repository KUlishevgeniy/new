#написать алгоритм сортировки

from random import randint
n = int(input())
a = [randint(0, 101) for i in range(n)]
print(a)

for i in range(n):
    for j in range(i+1, n):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]

for i in range(n):
    print(a[i], end=' ')
