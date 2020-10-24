with open("dados.csv",'r') as arquivo:
    arquivo.read()
    arquivo.replace(',','	')
with open('dados.tsv','w') as arquivo:
    arquivo.write(b)
    
    
    