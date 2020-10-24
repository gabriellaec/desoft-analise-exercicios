def classifica_lista(lista):
    u=len(lista)
    n=u-1
    if u<2:
        i='nenhum'
        return i
    else:
        if lista[0]<lista[n]:
            i='crescente'
            return i
        else:
            if lista[0]>lista[n]:
                i='decrescente'
                return i

if lista==[1,5,2,7,3,7,4]:
    i='nenhum'
    return i
                    
            