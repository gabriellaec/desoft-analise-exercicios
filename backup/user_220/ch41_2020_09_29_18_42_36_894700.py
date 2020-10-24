lista=[-3,-4,-2,-5,-1,0,1,-2,3,4]
def zera_negativos(lista):
    t=0
    while t < len(lista):
        if lista[t] < 0:
            lista[t]=0
            t+=1
        else:
            t+=1 
    return lista
