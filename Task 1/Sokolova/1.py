#### Написать алгоритм сортироки
#####

def bubble_sort(data: list) -> list:
    print("Исходные данные ", data)
    try:
        assert isinstance(data, list)
    except AssertionError:
        print("ОШИБКА")
        exit(1)
    for i in range(0, len(data)-1):
        for j in range(i, len(data)-1):
            try:
                if data[j] > data[j+1]:
                    data[j], data[j+1] = data[j+1], data[j]
            except TypeError:
                    print ("ОШИБКА")
                    exit(2)
        print(data)
    return data