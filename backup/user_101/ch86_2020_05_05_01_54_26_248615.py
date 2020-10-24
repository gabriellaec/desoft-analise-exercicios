arquivo = open('dados.csv', 'r')
conteudo = arquivo.read()
arquivo.close()

t = conteudo.replace(',', '\t')
with open('dados.tsv', 'w') as novo:
    c = novo.write(t)