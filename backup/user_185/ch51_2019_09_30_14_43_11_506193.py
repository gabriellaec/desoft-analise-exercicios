def estritamente_crescente(lista_input):
    i = 1
    lista_crescente = []
    lista_crescente.append(lista_input[0])
    while i < len(lista_input):
        if lista_input[i] > lista_input[i - 1]:
            lista_crescente.append(lista_input[i])
        i = i + 1
    return lista_crescente
            