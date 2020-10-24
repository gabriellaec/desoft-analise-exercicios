with open('dados.csv', 'r') as arquivo:
    conteudo = arquivo.read()

with open('dados.tsv', 'r') as arquivo:   
    conteudo2 = conteudo.replace(',' , '\t')

