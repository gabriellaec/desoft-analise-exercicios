with open('dados.csv', 'r') as csv:
    texto=csv.read()
final=texto.split(',')
end=(''.join(final))
with open('dados.tsv', 'w') as tsv:
    tsv.write(end)