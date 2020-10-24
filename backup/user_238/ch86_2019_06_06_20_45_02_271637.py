import csv
with open("dados.csv") as lista:
    conteudo=csv.reader(lista)
    for row in conteudo:
    	e="\t".join(row)
    
with open("dados.tsv","a") as arquivo:
    arquivo.write(e)
