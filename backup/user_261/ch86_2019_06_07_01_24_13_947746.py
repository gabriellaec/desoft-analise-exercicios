with open("dados.csv",'r') as arquivo:
    a=arquivo.read()
    b=arquivo.replace(',','	')
with open('dados.tsv','w') as arquivo:
    arquivo.write(b)
    
    
    