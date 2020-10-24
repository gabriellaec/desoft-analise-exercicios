def estritamente_crescente (lista):
    i = 0
    lista2 = []
    while i < len(lista):
        if lista[i] < lista[i+1]:
            lista2.append(lista[i], lista[i+1])
            i+=1
        else:
            i+=1
    return lista2
                          
            