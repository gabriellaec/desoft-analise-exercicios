with open('dados.csv') as d:
    texto=d.read()
    texto=texto.replace(',','\t')
    print(texto)