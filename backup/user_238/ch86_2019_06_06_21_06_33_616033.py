import csv
with open("dados.csv","w") as lista:
    conteudo=csv.reader(lista)
    for row in conteudo:
    	row="	".join(row)
    
with open("dados.tsv","a") as arquivo:
    arquivo.write(row)
