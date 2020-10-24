with open('dados.csv','r') as csvizinho:
    cont = csvizinho.split()
tsvizinho = cont.join('\t')
with open('dados.tsv','w') as tsvs:
    tsvs.write(tsvizinho)