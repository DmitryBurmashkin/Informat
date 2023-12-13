# Напишите функцию read_last(lines, file), которая будет открывать определенный файл file и выводить на печать
# построчно последние строки в количестве lines (на всякий случай проверим, что задано положительное целое число).
# Протестируем функцию на файле article.txt со следующим содержимым:
try:
    file = open('./file.txt')
except IOError:
    print('no file.txt')
lines = int(input('Введите число строк\n'))


def read_last(lines, file):
    k = 0
    stroki = file.readlines()
    for j in range(1, lines + 1):
        print(stroki[-j])


read_last(lines, file)
# Требуется создать csv-файл rows_300.csv со следующими столбцами:
# – № - номер по порядку (от 1 до 300);
# – Секунда – текущая секунда на вашем ПК;
# – Микросекунда – текущая миллисекунда на часах.
# На каждой итерации цикла искусственно приостанавливайте скрипт на 0,01 секунды.
import csv
import datetime
import time

Table = open('rows_300.csv', 'a+')
file_writer = csv.writer(Table, delimiter=',', lineterminator='\r')
headers = csv.DictWriter(Table, fieldnames=['№', 'Milisec', 'Sec'], delimiter=',')
headers.writeheader()
for i in range(300):
    current_time = datetime.datetime.now()
    type(current_time.microsecond) is int
    miliseconds = int(current_time.microsecond/1000)
    file_writer.writerow([i, miliseconds, current_time.second])
    time.sleep(0.01)
