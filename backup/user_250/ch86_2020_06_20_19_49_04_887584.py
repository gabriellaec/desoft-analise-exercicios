with open('dados.csv', 'r') as arquivo:
    conteudo = arquivo.read()
    conversao = conteudo.replace(',', '\t')
    with open('dados.tsv', 'w') as arquivo_final:
        arquivo_final.write(conversao)