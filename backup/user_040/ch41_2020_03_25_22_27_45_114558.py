lista=[]
def zera_negativos(lista):
    x=0
    if len(lista)>0:
        while x<len(lista):
            if lista[x]<=0:
                return lista[x] = 0
            else:
                return lista[x]
            x+=1
    else:
        return None
    