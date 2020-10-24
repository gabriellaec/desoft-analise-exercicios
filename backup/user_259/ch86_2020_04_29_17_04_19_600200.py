with open('dados.csv', 'r') as arquivo:
    conteudo = arquivo.read()
conteudo = conteudo.replace(',','\t')
with open('dados.tsc','w') as novo_arquivo:
    novo_arquivo.write(conteudo)

                    