def numero_no_indice(lista):
    igual = []
    i = 0
    for i in range(len(lista)):
        for j in lista:
            if i == j:
                igual.append(j)
    return igual