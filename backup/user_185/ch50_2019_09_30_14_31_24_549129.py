def numero_no_indice(lista_input):
    lista_output = []
    i = 0
    while i < len(lista_input):
        if lista_input[i] == i:
            lista_output.append(i)
        i = i + 1
    return lista_output

        