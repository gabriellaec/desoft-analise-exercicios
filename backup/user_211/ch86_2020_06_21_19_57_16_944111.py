import os
with open ('dados.csv','r') as arquivo:
    conteudo = arquivo.read()
    semvirgula=conteudo.replace(',','	')

with open("dados.tsv", "w") as novo:
    novo.write(semvirgula)