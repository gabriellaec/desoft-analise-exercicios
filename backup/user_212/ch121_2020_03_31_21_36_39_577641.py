def subtracao_de_listas (lista1, lista2):
    i= 0
    u= 0    
    b=len(lista2)
    c= len(lista1)
    while (c>i):
        if u<b:
            if lista1[i] != lista2[u]:
                u += 1
            elif lista1[i] == lista2[u]:
                del lista1[i]
                u = 0
                c=len(lista1)
        else:
            u=0
            i +=1
            
    return lista1