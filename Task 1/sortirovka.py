mas = []
N = int(input('Введите количество элементов массива: '))
for i in range(0,N):
    mas.append(int(input('Введите элемент массива: ')))
print(mas)

i = 0
while i < N - 1:
    j = 0
    while j < N - 1 - i:
        if mas[j] > mas[j + 1]:
            mas[j], mas[j + 1] = mas[j + 1], mas[j]
        j += 1
    i += 1

print(mas)