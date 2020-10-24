j=len(lista)
zera_negativos=[0]*j
i=0
while i<j:
    if lista[i]<0:
        zera_negativos[i]=lista[i]*(-1)
    else:
        zera_negativos[i]=lista[i]
    i+=1