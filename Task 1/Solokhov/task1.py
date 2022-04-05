def bubsort(mas, flag, num):
    for i in range(num):
        for j in range(1, num-i):
            if (flag == 0 and mas[j - 1] > mas[j]) or (flag == 1 and mas[j - 1] < mas[j]):
                buf = mas[j - 1]
                mas[j - 1] = mas[j]
                mas[j] = buf
    return mas
print("Введите размер массива: ")
num = int(input())
mas = [0]*num
print("Выберите сортировку(0 - по возрастанию, 1 - по убыванию): ")
flag = int(input())
for i in range(num):
    print("Введите ", i+1, " элемент массива: ")
    mas[i] = int(input())
mas = bubsort(mas, flag, num)
print(mas)