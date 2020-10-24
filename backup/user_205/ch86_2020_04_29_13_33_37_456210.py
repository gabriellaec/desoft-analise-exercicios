with open('dados.csv', 'r') as arquivo:
    conteudo = arquivo.read()
    with open('dados.tsv','w') as arquivo_tsv:
        troca = conteudo.replace(',','\t')
        fim = arquivo_tsv.write(troca)
