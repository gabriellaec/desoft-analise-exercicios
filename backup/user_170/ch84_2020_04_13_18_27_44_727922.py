def inverte_dicionario(lista):
    lista_invertida = {}
    for n, i in lista.items():
        if not i in lista_invertida:
            lista_invertida[i] = [n]
        else:
            lista_invertida[i].append(n)
    return lista_invertida