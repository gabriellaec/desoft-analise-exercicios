with open('dados.csv','r') as d:
    texto=d.read()
with open('dados.tsv','w') as t:
    texto=texto.replace(',','	')
    f=t.write(texto)
    