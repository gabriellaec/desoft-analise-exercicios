with open('dados.csv', 'r') as arquivo:
    conteudo = arquivo.read()
conteudo = conteudo.replace(',','	')
with open('dados.tsv','w') as novo_arquivo:
    novo_arquivo.write(conteudo)

                    