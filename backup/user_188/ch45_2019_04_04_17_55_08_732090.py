def zera_negativos(lista):
    lista_zerada = []
    contador = 0
    while contador < len(lista):
        if lista[contador] < 0:
            lista_zerada.append(0)
        else:
            lista_zerada.append(lista[contador])
        contador += 1
    return lista_zerada