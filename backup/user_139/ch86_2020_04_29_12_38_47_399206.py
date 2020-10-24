with open('dados.csv', 'r') as arquivo:
    conteudo = arquivo.read()
with open('dados.tsv', 'a') as arquivo:
    conteudo.replace(',', '\t')
    arquivo.write(conteudo)