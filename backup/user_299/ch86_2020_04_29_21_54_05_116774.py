with open('dados.csv','r') as csvizinho:
    cont = csvizinho.read(',')
    listadestrings = cont.split
tsvizinho = listadestrings.join('\t')
with open('dados.tsv','w') as tsvs:
    tsvs.write(tsvizinho)