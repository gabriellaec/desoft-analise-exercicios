def numero_no_indice(lista):
    i = 0
    lista_verdadeira = []
    while i < len(lista):
        if lista[i] == i:
            lista_verdadeira.append(lista[i])
        i += 1
    return lista_verdadeira