#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = [ 'мама','папа','кот']


# список списков приблизителного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
    [ 'мама', 168],
    [ 'папа', 181],
    [ 'кот', 30],
]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
print('Рост отца - ', my_family_height[1][1], 'см')

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
print( 'Совместный рост нашей семьи - ', my_family_height[0][1]+my_family_height[1][1]+my_family_height[2][1], 'см. Нифига, как индийский слон ростом')