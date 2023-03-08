import csv
from collections import OrderedDict as dic

with open("stage3_test.csv", 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f, delimiter=',')
    price_dict = {}
    for row in reader:
        price_dict[row["Title"]] = float(row["Price"])

norm_dict = dic(sorted(price_dict.items(), key=lambda t: t[1]))
flipped_dict = dic(sorted(price_dict.items(), key=lambda t: t[1], reverse=True))

print(norm_dict, flipped_dict)