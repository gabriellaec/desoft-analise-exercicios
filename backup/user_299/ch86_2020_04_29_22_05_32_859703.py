with open('dados.csv','r') as csvizinho:
    cont = csvizinho.read()
    listadestrings = cont.split(',')
tsvizinho = '\t'.join(listadestrings)
with open('dados.tsv','w') as tsvs:
    tsvs.write(tsvizinho)