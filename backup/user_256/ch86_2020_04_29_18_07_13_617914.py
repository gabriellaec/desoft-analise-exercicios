with open ('dados.csv', 'r') as arquivo:
    leitura = arquivo.read()
with open('dados.tsv', 'r') as novo:
    va = leitura.repleace(',' , '\t')
    novo.write(va)
    