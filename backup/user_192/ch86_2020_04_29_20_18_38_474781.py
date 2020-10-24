with open('dados.csv', 'r') as arquivo:
    conteudo = arquivo.read()

dados.tsv = conteudo.replace(',' , '\t')

with open('dados.tsv', 'r') as arquivo:
    conteudo2 = arquivo.read()
