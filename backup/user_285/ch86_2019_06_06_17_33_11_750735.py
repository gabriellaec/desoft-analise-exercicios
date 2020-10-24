with open('dados.csv', 'r') as csv:
    texto=csv.read()
texto1=texto.split(',')
texto2=(''.join(texto1))
with open('dados.tsv', 'w') as tsv:
    tsv.write(texto2)