def numero_no_indice(Lista):
    soma = []
    Lista = list
    i = 0
    while i < len(Lista):
        if Lista[i] == i:
            soma.append(Lista[i])
            i = i + 1
        if Lista[i] != i:
            i = i + 1
    return soma
