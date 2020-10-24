def estritamente_crescente(lista):
    i=0
    while i<len(lista):
        if lista[i]>lista[i-1]:
            lista.append(lista[i])
        i+=1
    return lista[i]