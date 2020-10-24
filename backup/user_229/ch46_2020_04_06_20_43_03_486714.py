def numero_no_indice(lista):
    numero = []
    for i in lista:
        if i == lista[i]:
            numero.append(i)
    return numero