def numero_no_indice (lista):
    iguais = []
    i = 0
    while i < len(lista):
        if lista[i] == i:
            iguais.append(lista[i])
            i += 1
        else: 
            i += 1
    return iguais