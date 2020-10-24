def subtracao_de_listas(lista1, lista2):
    soma = lista1 + lista2
    i = 0
    lista_nova = []
    while i < len(soma):
        if soma[i] not in lista_nova:
            if soma[i] not in lista2:
                lista_nova.append(soma[i])
        i += 1
    return lista_nova