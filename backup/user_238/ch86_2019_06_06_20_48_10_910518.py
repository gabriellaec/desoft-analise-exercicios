import csv
with open("dados.csv","r") as lista:
    conteudo=csv.reader(lista)
    for row in conteudo:
    	row="	".join(row)
    
with open("dados.tsv","a") as arquivo:
    arquivo.write(row)
