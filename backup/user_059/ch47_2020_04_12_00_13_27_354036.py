def estritamente_crescente(lista):
    l = []
    i = 0 
    while i<len(lista):
        if lista[i]<lista[i-1]:
            l.append(lista[i])
    return l
            