n = int(input())
a = [int(input()) for i in range(n)]
for i in range(n - 1):
    for j in range(n - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
        j += 1
print(a)
