with open ('dados.csv', 'r') as arquivo:
    leitura = arquivo.read()
    sub = leitura.write()
    novo = sub.replace(',' , '	')
    novo.close as 'dados.tsv'