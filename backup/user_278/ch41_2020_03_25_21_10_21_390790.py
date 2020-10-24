lista=[-2,-3,5,-7,9]
def zera_negativos(lista):
    i=0
    while i<len(lista):
        if lista[i]<0:
            lista[i]=0
        else:
            lista[i]=lista[i]
        i+=1
print (zera_negativos(lista))