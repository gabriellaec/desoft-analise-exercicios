import csv

with open("dados.csv", "r") as dados:
    conteudo = dados.read()
    
with open("dados.tsv", "w") as arquivo:
    arquivo.write(conteudo.replace(",", "\t"))