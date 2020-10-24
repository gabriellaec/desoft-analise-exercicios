with open('dados.csv', 'r') as arquivo:
    conteudo = arquivo.read()
tsv = conteudo.replace(',','	')
with open('dados.tsv', 'w') as conversao:
    conversao.write(tsv)

                    