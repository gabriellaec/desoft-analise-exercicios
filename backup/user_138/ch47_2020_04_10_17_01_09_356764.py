def estritamente_crescente(lista):
    i=0
    while i<len(lista):
        if lista[i+1]>lista[i]:
            lista.append(lista[i])
        i+=1
    return lista[i]