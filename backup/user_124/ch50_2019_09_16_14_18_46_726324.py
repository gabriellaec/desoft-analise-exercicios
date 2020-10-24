def numero_no_indice(lista):
    i = 0
    lista = []
    lista_verdadeira = []
    while i < len(lista):
        if lista[i] == lista.index():
            lista_verdadeira.append(lista[i])
            i += 1
    return lista_verdadeira
            