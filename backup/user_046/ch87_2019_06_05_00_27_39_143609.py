with open('churras.txt','r') as arquivo:
	lines=rquivo.readlines()
    multi=[]
    saida=[]
    line=lines.split(';')
    for linha in line:
        saida.append(int(line[1]))
        saida.append(float(line[2]))
    	multi.append(saida[0]*saida[1])
    	valor=sum(multi)
    print(valor)
    
        

                          
                 
     
        
	