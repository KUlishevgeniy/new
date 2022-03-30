from random import randint

N = 20
num = []
for i in range (N):
    num.append(randint(0, 500))
print(num)

for i in range (N-1):
    for j in range(N-i-1):
        if num[j] > num[j+1]:
            num[j], num[j+1] = num[j+1], num[j]
print(num)