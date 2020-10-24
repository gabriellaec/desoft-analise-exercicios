with open('dados.csv','r') as arquivo:
    a=arquivo.read() 
with open('dados.tsv','w') as arquivo2:
    c=a.replace(',','	')
    b=arquivo2.write(c)

