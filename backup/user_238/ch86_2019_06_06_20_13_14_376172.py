import csv
with open("dados.csv") as lista:
    conteudo=csv.reader(lista)
    e=' '.join(conteudo)
    
with open("dados.tsv","a") as arquivo:
    arquivo.write("e"\n)
