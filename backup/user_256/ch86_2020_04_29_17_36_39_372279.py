with open ('dados.csv', 'r') as arquivo:
    leitura = arquivo.read()
    novo = leitura.replace(',' , '\t')
    novo.close as 'dados.tsv'