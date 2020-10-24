with open ('dados.csv', 'r') as arquivo:
    conteudo = arquivo.read()
    conteudotsv = conteudo.replace(',', '\t')
    dados.tsv = conteudotsv
    print(dados.tsv)
    