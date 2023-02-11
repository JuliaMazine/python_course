import csv

with open("stage3_test.csv", 'r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=',')
    headers = next(reader, None)
    with open('cost.csv', 'w',encoding='utf-8') as f:

        writer = csv.writer(f, delimiter=',')
        if headers:
            writer.writerow(headers)
        for row in reader:

            if 10000 < float(row[-1]) <= 50000:
                writer.writerow(row)