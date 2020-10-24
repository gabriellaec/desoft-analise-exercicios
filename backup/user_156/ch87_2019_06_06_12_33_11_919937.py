import csv

with open("churras.txt", "r") as banana:
    conteudo = csv.reader (banana)
    i=0
    for row in conteudo:
        i+= float(row[1])*float(row[2])
    print (i)
        