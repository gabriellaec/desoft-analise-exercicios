with open ('dados.csv', 'r') as arquivo:
    conteudo = arquivo.read()
    substituição = conteudo.replace(',', '\t')
with open('dados.tsv', 'w'):
    