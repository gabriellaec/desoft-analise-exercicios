import csv
with open('churras.txt') as churras:
    total = 0
    for linha in list(csv.reader(churras)):
        total += float(linha[1]) + float(linha[2])

print(total)