import csv
with open('churras.txt') as churras:
    total = 0
    for linha in list(csv.reader(churras)):
        total += int(linha[1]) + float(linha[2])

print(total)