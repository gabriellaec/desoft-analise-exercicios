with open ('dados.csv', 'r') as arquivo:
    conteudo = arquivo.read()
tsv = conteudo.replace(',', '\t')
print(tsv)