with open ('dados.csv', 'r') as arquivo:
    conteudo = arquivo.read()
tsv = conteudo.replace(',', '	')
with open ('dados.csv', 'w') as arquivo2:
    arquivo2.write(tsv)