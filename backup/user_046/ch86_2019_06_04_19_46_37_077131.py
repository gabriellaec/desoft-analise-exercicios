f=open("dados.tsv")
with open('dados.csv','r') as arquivo:
    dados=arquivo.read()
    return dados

with open ('dados.tsv','w') as arquivo2:
    arquivo2.write(dados)
    
    
