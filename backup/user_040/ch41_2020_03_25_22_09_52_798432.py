def zera_negativos(lista):
    x=0
    if len(lista)>1:
        while x<len(lista):
            if lista[x]<=0:
                return 0
            else:
                return lista[x]
            x+=1
    else:
        return None
    