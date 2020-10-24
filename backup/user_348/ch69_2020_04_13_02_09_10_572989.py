def junta_listas (lista):
    lista_simples = []
    for numero in lista:
        for i in numero:
            j = numero[i]
            lista_simples.append(j)
    return lista_simples