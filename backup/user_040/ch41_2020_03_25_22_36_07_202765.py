lista=[]
def zera_negativos(lista):
    x=0
    if len(lista)>0:
        while x<len(lista):
            if lista[x]<=0:
                lista[x] = 0
            else:
                lista[x]=lista[x]
            x+=1
    else:
        return None
    return lista
