def numero_no_indice(lista):
    indicelista = []
    i = 0
    while i < len(lista):
        if i == lista[i]:
            indicelista.append(lista[i])
            i += 1
        else:
            i += 1
    return indicelista