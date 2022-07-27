import csv
with open('output.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        for i in row:
            if i != '':
                print(i)

