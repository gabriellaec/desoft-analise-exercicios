def estritamente_crescente (lista):
    i = 0
    lista2 = [lista[0]]
    while i < len(lista):
        if lista[0] < lista[i]:
            lista2.append(lista[i])
            i+=1
        else:
            i+=1
    return lista2
                          
            