import csv

with open ('dados.csv') as entrada, open ('dados.tsv','w') as saida:
    csvobas=csv.reader(entrada) 
    for row in csvobas:
        t1=row.split(',')
        t2=t1.join("	")
        saida.writerow(t2)

    
