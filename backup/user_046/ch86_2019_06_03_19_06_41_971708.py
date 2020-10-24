f=open("dados.tsv")
with open('dados.csv') as arquivo:
    dados=arquivo.read()
    return dados
with open ('dados.tsv','w') as arquivo2:
    arquivo.write(dados)
    
    
