#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['я', 'мама', 'папа', 'бабушка']


# список списков приблизителного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
    ['я', 185],
    ['мама', 170],
    ['папа', 190],
    ['бабушка', 160],
]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
print("Рост отца - ", my_family_height[2][1], " см")

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов

print("Общий рост моей семьи - ", my_family_height[0][1] + my_family_height[1][1] + my_family_height[2][1] + my_family_height[3][1], " см")