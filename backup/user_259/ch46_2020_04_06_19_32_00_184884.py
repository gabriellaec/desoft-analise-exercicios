def numero_no_indice(lista):
    iguais = []
    for i in range(len(lista)):
        for j in lista:
            if i == j:
                iguais.append(j)
    return iguais