def numero_no_indice(lista):
    igual = []
    for i in range(len(lista)):
        if i == lista[i]:
            igual.append(i)
    return igual