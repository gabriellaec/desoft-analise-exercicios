lista=[0]*100
lista[0]=1
soma=0
i=0
while i<len(lista):
    lista[i+1]=lista[i]/2
    soma+=lista[i]
    i+=1
    