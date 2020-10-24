def estritamente_crescente (lista):
    lista2 = []
    i = 0
    x = 1
    lista2.append(lista[0])
    while i+x<len(lista):        
        if lista[i+x]>lista[i]:        
            lista2.append(lista[i+x])
        else:
            x+=1
        i+=1
    print (lista2)
    return lista2