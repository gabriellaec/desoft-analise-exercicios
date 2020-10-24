with open('dados.csv', 'r') as arquivo:
    conteudo = arquivo.read()

novo_conteudo = conteudo.replace(',','\t')

with open('dados.tsv', 'w') as arquivo2:
    arquivo2.write (novo_contedo)