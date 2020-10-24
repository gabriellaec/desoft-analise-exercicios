def quantos_uns(x):
    x=str(x)
    i=0
    contador=0
    while i<len(x):
        if x[i]=='1':
            contador+=1		
        i+=1
	return contador
            
    