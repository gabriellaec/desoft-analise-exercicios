with open('dados.csv','r') as lido:
    original = lido.read()

with open('dados.tsv','w') as escrito:
    convertido = escrito.write(original)
    