def numero_no_indice(lista):
    indice = [i for i in range(len(lista))]
    iguais = []
    for i in lista:
        for j in indice:
            if i == lista[i]:
                iguais.append(lista[i])
    return iguais
        