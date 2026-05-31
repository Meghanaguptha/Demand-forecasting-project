import os
import csv
import random
from datetime import datetime, timedelta

os.makedirs('data', exist_ok=True)

stores = list(range(1, 11))
store_types = ['a', 'b', 'c', 'd']
assortments = ['a', 'b', 'c']
promo_intervals = ['Jan,Apr,Jul,Oct', 'Feb,May,Aug,Nov', 'Mar,Jun,Sept,Dec', '']

with open('data/store.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Store','StoreType','Assortment','CompetitionDistance','CompetitionOpenSinceMonth','CompetitionOpenSinceYear','Promo2','Promo2SinceWeek','Promo2SinceYear','PromoInterval'])
    for s in stores:
        writer.writerow([
            s,
            random.choice(store_types),
            random.choice(assortments),
            random.randint(100, 2000),
            random.randint(1, 12),
            random.randint(2005, 2023),
            random.choice([0,1]),
            random.randint(1, 52),
            random.randint(2005, 2023),
            random.choice(promo_intervals)
        ])

start = datetime(2025, 1, 1)
rows = []
for store in stores:
    for i in range(40):
        date = start + timedelta(days=i)
        dayofweek = date.isoweekday()
        open_flag = 0 if date.weekday() == 6 else 1
        promo = 1 if random.random() < 0.3 else 0
        stateholiday = random.choice(['0', 'a', 'b', 'c']) if random.random() < 0.1 else '0'
        sales = 0 if open_flag == 0 else int(max(0, random.gauss(8000 + promo*2000, 1800)))
        customers = 0 if sales == 0 else max(10, int(sales / random.uniform(8, 12)))
        rows.append([store, dayofweek, date.strftime('%Y-%m-%d'), sales, customers, open_flag, promo, stateholiday, 0])

with open('data/train.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Store','DayOfWeek','Date','Sales','Customers','Open','Promo','StateHoliday','SchoolHoliday'])
    writer.writerows(rows)

with open('data/test.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Store','DayOfWeek','Date','Open','Promo','StateHoliday','SchoolHoliday'])
    test_start = start + timedelta(days=41)
    for store in stores:
        for i in range(10):
            d = test_start + timedelta(days=i)
            open_flag = 0 if d.weekday() == 6 else 1
            writer.writerow([store, d.isoweekday(), d.strftime('%Y-%m-%d'), open_flag, 1 if random.random() < 0.3 else 0, '0', 0])

print('Sample dataset files created: data/train.csv, data/store.csv, data/test.csv')
