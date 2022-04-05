a = list(map(int, input().split())) #вводим массив в строчку
l = len(a)
for i in range(l-1):
    for j in range(l-1-i):
        if a[j] > a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]
print(*a)
