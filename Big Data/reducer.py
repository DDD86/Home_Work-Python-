import sys

total_price = 0
total_count = 0
price_squared_sum = 0

for line in sys.stdin:
    parts = line.strip().split('\t')
    if len(parts) == 2:
        key, value = parts
        try:
            price = float(value)
            total_price += price
            price_squared_sum += price ** 2
            total_count += 1
        except ValueError:
            continue

mean_price = total_price / total_count if total_count > 0 else 0
variance = (price_squared_sum / total_count) - (mean_price ** 2) if total_count > 0 else 0

print('Mean Price:', mean_price)
print('Variance:', variance)
