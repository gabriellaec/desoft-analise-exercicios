int(lista)=[]
def zera_negativos(lista):
    n=len(lista)
    i=0
    while i<=n-1:
        if lista[i]<0:
            lista[i]=0
            i+=1
        else:
            i+=1
	return lista
       
        
        