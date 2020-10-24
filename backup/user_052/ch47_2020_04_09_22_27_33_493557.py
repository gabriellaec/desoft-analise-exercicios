def estritamente_crescente (lista):
    i = 0
    lista2 = []
    while i < len(lista):
        if lista[0] < lista[1]:
            lista2.append(lista[0])
            lista2.append(lista[1])
            i+=1
            if lista[1] < lista[i]:
                lista2.append(lista[i])
                i+=1
        else:
            i+=1
    return lista2
                          
            