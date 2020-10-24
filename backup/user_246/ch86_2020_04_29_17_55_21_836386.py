with open('dados.csv','r') as d:
    texto=d.read()
    texto=texto.replace(',','\t')
with open('dados.tsv','w') as t:
    f=t.write(texto)
    