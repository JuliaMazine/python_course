import csv

with open("stage3_test.csv", 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f, delimiter=',')

    with open('3images.csv', 'w',encoding='utf-8') as f:
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in reader:
            if len((row['Images']).split(',')) > 3:
                writer.writerow(row)