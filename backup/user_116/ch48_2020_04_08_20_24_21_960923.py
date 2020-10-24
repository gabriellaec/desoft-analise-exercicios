def eh_crescente(lista):
    i=0
    u=1
    while u< len(lista):
        if lista[u]>lista[i]:       
            u+=1
            i=u-1
       
        else:
            return False
    return True      
