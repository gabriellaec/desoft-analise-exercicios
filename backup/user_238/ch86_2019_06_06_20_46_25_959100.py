import csv
with open("dados.csv") as lista:
    conteudo=csv.reader(lista)
    for row in conteudo:
    	"	".join(row)
    
with open("dados.tsv","a") as arquivo:
    arquivo.write(conteudo)
