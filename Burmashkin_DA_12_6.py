#Дан двумерный массив размером 3x3. Определить максимальное значение среди элементов третьего столбца массива; максимальное значение среди элементов второй строки массива. Вывести полученные значения.
n = 3
arr = list()
for i in range(n):
  brr = list()
  for i in range(n):
    brr.append(int(input()))
  arr.append(brr)
for i in range(n):
  for j in range(n):
    print(arr[i][j], end=' ')
  print()
stroka2 = list()
stolbec3 = list()
stroka2.append(int(arr[1][0]))
stroka2.append(int(arr[1][1]))
stroka2.append(int(arr[1][2]))
print(max(stroka2))
stolbec3.append(int(arr[0][2]))
stolbec3.append(int(arr[1][2]))
stolbec3.append(int(arr[2][2]))
print(max(stolbec3))
#Дан двумерный массив размером mxn. Сформировать новый массив заменив положительные элементы единицами, а отрицательные нулями. Вывести оба массива.
m = int(input('Задание 2\n Введите число строк матрицы\n'))
n = int(input('Введите число столбцов матрицы\n'))
arr = list()
for i in range(m):
  brr = list()
  for i in range(n):
    brr.append(int(input()))
  arr.append(brr)
for i in range(m):
  for j in range(n):
    print(arr[i][j], end = ' ')
  print()
for i in range(m):
  for j in range(n):
    if arr[i][j] >0:
      arr[i][j]=1
    elif arr[i][j] < 0:
      arr[i][j]=0
for i in range(m):
  for j in range(n):
    print(arr[i][j], end =' ')
  print()
#Дана целая квадратная матрица n-го порядка. Определить, является ли она магическим квадратом, т. е. такой матрицей, в которой суммы элементов во всех строках и столбцах одинаковы.
n = int(input('Задание 3\n Порядок квадратной матрицы:\n'))
arr = list()
for i in range(n):
  brr = list()
  for i in range(n):
    brr.append(int(input()))
  arr.append(brr)
for i in range(n):
  for j in range(n):
    print(arr[i][j], end = ' ')
  print()
sumstroki = list()
sumstolbcov = list()
for i in range(n):
  for j in range(n):
    type(arr[i][j]) is int
    type(arr[j][i]) is int
    sumstroki.append(arr[i][j])
    sumstolbcov.append(arr[j][i])
if sum(sumstroki) == sum(sumstolbcov):
  print('Это магический квадрат!')
#Определить, является ли заданная целая квадратная матрица n-го порядка симметричной (относительно главной диагонали).
n = int(input('Задание 4\n Порядок квадратной матрицы:\n'))
arr = list()
for i in range(n):
  brr = list()
  for i in range(n):
    brr.append(int(input()))
  arr.append(brr)
for i in range(n):
  for j in range(n):
    print(arr[i][j], end = ' ')
  print()
Upper = list()
lower = list()
for i in range(n):
  for j in range(n):
    if i < j:
      type(arr[i][j]) is str
      Upper.append(arr[i][j])
    elif i > j:
      lower.append(arr[i][j])
if Upper == lower:
  print('Это симметричная относительно главной диагонали матрица')
else:
  print('Это не симметричная относительно главной диагонали матрица')
#Дана прямоугольная матрица. Найти строку с наибольшей и строку с наименьшей суммой элементов. Вывести на печать найденные строки и суммы их элементов.
m = int(input('Задание 5\n Введите число строк матрицы\n'))
n = int(input('Введите число столбцов матрицы\n'))
arr = list()
for i in range(m):
  brr = list()
  for i in range(n):
    brr.append(int(input()))
  arr.append(brr)
for i in range(m):
  for j in range(n):
    print(arr[i][j], end = ' ')
  print()
stroki = list()
sumstroki = list()
stolbci = list()
sumstolbcov = list()
for i in range(m):
  stroki = 0
  for j in range(n):
    type(arr[i][j]) is int
    stroki += arr[i][j]
  sumstroki.append(stroki)
for i in range(n):
  stolbci = 0
  for j in range(m):
    type(arr[j][i]) is int
    stolbci += arr[j][i]
  sumstolbcov.append(stolbci)
print ('Наибольший столбец:', sumstolbcov.index(max(sumstolbcov))+1)
print ('Наибольшая строка::', sumstroki.index(max(sumstroki))+1)
#Дана действительная матрица размером n х m, все элементы которой различны. В каждой строке выбирается элемент с наименьшим значением. Если число четное, то заменяется нулем, нечетное - единицей. Вывести на экран новую матрицу.
n = int(input('Задание 6\n Число строк:\n'))
m = int(input('Число столбцов:\n'))
arr = list()
for i in range(n):
  brr = list()
  for i in range(m):
    brr.append(int(input()))
  arr.append(brr)
for i in range(n):
  for j in range(m):
    print(arr[i][j], end = ' ')
  print()
for i in range(n):
  for j in range(m):
    y = list()
    y.append(j)
    k = y.index(min(y))
    if arr[i][k] % 2 == 0:
      arr[i][k] = 0
    else:
      arr[i][k] = 1
for i in range(n):
  for j in range(m):
    print(arr[i][j], end = ' ')
  print()













