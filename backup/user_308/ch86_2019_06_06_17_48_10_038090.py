import csv

with open ('dados.csv') as entrada, open ('dados.tsv','w') as saida:
    csvobas=csv.reader(entrada) 
    for row in csvobas:
        x=row.join("	")
        saida.writerow(x)

    
