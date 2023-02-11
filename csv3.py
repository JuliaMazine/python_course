import csv

with open("stage3_test.csv", 'r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=',')

    with open('skinny.csv', 'w',encoding='utf-8') as f:
        writer = csv.writer(f)
        for row in reader:
            writer.writerow([row[0], row[2], row[4]])