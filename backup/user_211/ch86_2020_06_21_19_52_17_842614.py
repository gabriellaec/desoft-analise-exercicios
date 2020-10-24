import os
with open ('dados.csv','r') as arquivo:
    conteudo = arquivo.read()
    semvirgula=conteudo.replace(',','\t')
with open('dados.csv','w') as arquivo:
    arquivo.write(semvirgula)
    os.rename('dados.csv','dados.tsv')