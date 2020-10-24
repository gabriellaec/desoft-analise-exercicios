with open('dados.csv','r') as d:
    texto=d.read()
    texto=texto.replace(',','	')
    texto=open('dados.tsv','w+')
    
    