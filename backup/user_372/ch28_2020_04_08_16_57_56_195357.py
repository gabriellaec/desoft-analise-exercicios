lista=[0]*100
soma=0
i=0
while i<len(lista):
    lista[i]=1/(2**i)
    soma+=lista[i]
    i+=1
    