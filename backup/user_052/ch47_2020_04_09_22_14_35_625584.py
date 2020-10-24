def estritamente_crescente (lista):
    i = 1
    lista2 = []
    while i < len(lista):
        if lista[i-1] < lista[i]:
            lista2.append(lista[i-1])
            i+=1
        else:
            i+=1
    return lista2
                          
            