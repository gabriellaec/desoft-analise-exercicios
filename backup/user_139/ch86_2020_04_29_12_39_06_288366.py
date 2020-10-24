with open('dados.csv', 'r') as arquivo:
    conteudo = arquivo.read()
with open('dados.tsv', 'a') as arquivo:
    a = conteudo.replace(',', '	')
    arquivo.write(a)