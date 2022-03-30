#Сортировка пузырьком

from random import randint

m = 10
q = []
for i in range(m):
    q.append(randint(1, 50))
print(q)

for i in range(m - 1):
    for j in range(m - i - 1):
        if q[j] > q[j + 1]:
            q[j], q[j + 1] = q[j + 1], q[j]

print(q)
