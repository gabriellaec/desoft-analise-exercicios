def numero_no_indice(lista):
    l = []
    i = 0
    while i < len(lista):
        if lista[i] == i:
            l.append(lista[i])
        i+=1
    return l
    
