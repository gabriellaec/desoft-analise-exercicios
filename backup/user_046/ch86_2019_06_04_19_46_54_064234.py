f=open("dados.tsv")
with open('dados.csv','r') as arquivo:
    dados=arquivo.read()
    	

with open ('dados.tsv','w') as arquivo2:
    arquivo2.write(dados)
    
    
