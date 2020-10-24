with open('dados.csv', 'r') as csv:
    texto=csv.read()
    final=texto.split(',')
with open('dados.tsv', 'w') as tsv:
    tsv.wirte(final)