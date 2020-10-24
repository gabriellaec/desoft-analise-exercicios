def numero_no_indice(lista) :
    i = 0
    nova = []
    while i < len(lista) :
        if i == lista[i] :
            nova.append(lista[i])
        i += 1
        
    return nova
        
    