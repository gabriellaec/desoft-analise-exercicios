import csv
total = 0
with open('churras.txt', 'r') as arquivo:
    csv_reader = csv.reader(arquivo, delimiter=',')
    for line in csv_reader:
        custo = line[1]*line[2]
        total+=custo
print(total)
