with open('dados.csv', 'r') as csv:
    texto=csv.read()
with open('dados.tsv', 'w') as tsv:
    tsv.write(texto)