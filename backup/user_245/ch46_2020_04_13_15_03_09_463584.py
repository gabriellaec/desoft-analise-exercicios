def numero_no_indice(lista):
    iguais = []
    for e in range(len(lista)):
        if e == lista[e]:
            iguais.append(lista[e])
    return iguais