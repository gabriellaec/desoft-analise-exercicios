import csv
with open('churras.txt') as churras:
    total = 0
    if len(list(csv.reader(churras))) > 2:
        for linha in list(csv.reader(churras)):
            total += float(linha[1]) + float(linha[2])
    

print(total)
