import sys
import csv
from statistics import mean

# Инициализация переменных для подсчета среднего значения и дисперсии
prices = []

# Считываем данные из CSV-файла
with open('AB_NYC_2019.csv', newline='', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  # Пропускаем заголовок
    for row in csvreader:
        # Извлекаем значение цены из каждой строки и добавляем его в список
        price = float(row[9])
        prices.append(price)

# Проверим, сколько значений было считано
print('Total Prices Count:', len(prices))

# Проверим, что список не пустой
if prices:
    # Вычисляем среднее значение и дисперсию
    mean_price = mean(prices)
    variance = sum((x - mean_price) ** 2 for x in prices) / len(prices)

    # Выводим результаты
    print('Mean Price:', mean_price)
    print('Variance:', variance)
else:
    print('No prices were read from the file.')