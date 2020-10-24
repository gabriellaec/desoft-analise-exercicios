with open('dados.csv', 'r') as arquivo:
    conteudo = arquivo.read()
with open('dados.tsv', 'a') as arquivo:
    arquivo.write(conteudo)