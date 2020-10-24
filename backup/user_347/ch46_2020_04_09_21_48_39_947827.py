def numero_no_indice(lista):
    o = []
    i = 0
    while i < len(lista):
        if lista[i] == i:
            
            o.append(lista[i])
            i+=1
        else:
            i+=1
    return o