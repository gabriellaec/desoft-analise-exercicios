with open('dados.csv','r') as arquivo:
    texto = arquivo.read()
    texto = texto.replace(',','\t')
    with open('dados.tsv','w') as arquivo_tsv:
        arquivo_tsv.write(texto)