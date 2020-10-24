def estritamente_crescente (lista):
    lista2 = []
    i = 0
    x = 1
    while i<len(lista):
        lista2.append(lista[0])
        if lista[i+x]>lista[i]:        
            lista2.append(lista[i+x])
            x+=1
        i+=1
        print (lista2)
    return lista2