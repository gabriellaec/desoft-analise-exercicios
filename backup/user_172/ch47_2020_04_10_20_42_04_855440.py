def estritamente_crescente (lista):
    lista2 = []
    i = 0
    x = 1
    if len(lista)>0:
        lista2.append(lista[0])     
    else:
        return lista2
    while i+x<len(lista):        
        if lista[i+x]>lista[i]:        
            lista2.append(lista[i+x])
            i+=1
            x==1
        else:
            x+=1
        
    print (lista2)
    return lista2