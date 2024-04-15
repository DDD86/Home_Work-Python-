import sys
import csv

with open('AB_NYC_2019.csv', newline='', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  # Пропускаем заголовок
    for row in csvreader:
        price = row[9]
        print('price\t%s' % price)





