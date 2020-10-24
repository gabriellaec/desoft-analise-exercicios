with open ('dados.csv', 'r') as arquivo:
    leitura = arquivo.read()
with open('dados.tsv', 'w') as novo:
    va = leitura.replace(',' , '\t')
    novo.write(va)
    