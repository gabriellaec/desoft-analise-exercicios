with open ('dados.csv', 'r') as arquivo:
    conteudo = arquivo.read()
    substituição = conteudo.replace(',', '	')
with open('dados.tsv', 'w') as arquivo2:
    arquivo2.write(substituição)
    