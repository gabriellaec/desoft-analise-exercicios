with open('churras.txt','r') as arquivo:
	line=arquivo.read()
    linhas=line.split(',')
    linhas.remove(0::3)
    total=[]
for quantidade,preco in linhas:
    total.append(linha[quantidade]*linha[preco])
    a=sum(total)
print(total)
    
    
        

                          
                 
     
        
	