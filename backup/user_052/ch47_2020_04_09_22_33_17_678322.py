def estritamente_crescente (lista):
    i = 1
    lista2 = [lista[0]]
    while i < len(lista):
        if lista [0] < lista[1]:
            lista2.append(lista[1])
            i +=1
            if lista[i] < lista[i+1]:
                lista2.append(lista[i+1])
                i+=1
        else:
            i+=1
    return lista2
                          
            