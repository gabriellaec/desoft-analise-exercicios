with open('dados.csv', 'r') as arquivo:
    conteudo = arquivo.read()
print(conteudo)
tsv = conteudo.replace(',','\t')
print(tsv)