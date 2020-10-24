valores=[-4, 3, 0, -2, 5]
i=0
def zera_negativos(valores):
    while i<len(valores):
    	if valores[i]<0:
        	valores[i]=0
    	i+=1
return zera_negativos