# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких 
# собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста ис двух соседнихс ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом 
# заданной во входном файле грядки.
# i: 4 -> 1 2 3 4 
# o: 9

garden_bed = []
n = int(input("Введите количество кустов: "))
for i in range(n):
    berries = int(input(f"Введите количество ягод на {i+1} кусте: "))
    garden_bed.append(berries)
print(f"Ваша грядка: {garden_bed}\n")

result = 0
for i in range(len(garden_bed)):
    current_sum = garden_bed[i] + garden_bed[(i + 1) % n] + garden_bed[(i + 2) % n]
    if current_sum > result:
        result = current_sum
print(f"Максимального число ягод, которое можно собрать: {result}")