import pandas as pd
import numpy as np
import random
from matplotlib import pyplot
# Создать объект pandas Series из листа, объекта NumPy, и словаря
print('Задание 1')
list1 = (random.randint(1, 100) for x in range(10))
numpy = np.array([1, 2, 3])
dictionary = dict(a='1', b='2')

my_series_list1 = pd.Series(list1)
print(my_series_list1, 'Это серия из списка')
my_series_numpy = pd.Series(numpy)
print(my_series_numpy, 'Это серия из одномерного массива нампая')
my_series_dictionary = pd.Series(dictionary)
print((my_series_dictionary), 'Это серия из словаря')

# Получить не пересекающиеся элементы в двух объектах Series
print('Задание 2')
set1 = set()

my_series1 = pd.Series(random.randint(2, 10) for x in range(5))
my_series2 = pd.Series(random.randint(2, 10) for x in range(5))
print(my_series1, 'Это первая серия')
print(my_series2, 'Это вторая серия')
for i in my_series1:
    for j in my_series2:
        if i != j:
            set1.add(i)
for j in my_series2:
    for i in my_series1:
        if j != i:
            set1.add(j)
print(set1)

# Узнать частоту уникальных элементов объекта Series (гистограмма)

print('Задание 3')

my_series3 = pd.Series(random.randint(1, 5) for x in range(100))
my_series3.plot.hist()
pyplot.savefig('frequencyBA.svg')

#Объединить два объекта Series вертикально и горизонтально

print('Задание 4')
my_series_4 = pd.Series(random.randint(10, 1000) for x in range(3))
my_series_5 = pd.Series(random.randint(10, 1000) for x in range(3))
print(my_series_4, 'Первая серия')
print(my_series_5, 'Вторая серия')
print(pd.concat([my_series_4, my_series_5]), 'Это вертикальное объединение')
print(pd.concat([my_series_4, my_series_5], axis= 1), 'Это горизонтальное объединение')

#Найти разность между объектом Series и смещением объекта Series на n

print('Задание 5')
my_series_6 = pd.Series(random.randint(10, 100) for x in range(5))
print(my_series_6, 'Это обычная серия')
n = int(input('Введите число смещений\n'))
print(my_series_6.diff(periods=n), 'Это разность между объектом Series и смещением объекта Series на n')

