def estritamente_crescente(lista):
    i = 0
    j = 0
    lista_resultado = [lista[0]]
    while i < len(lista):
        if lista[i] < lista[j]:
            lista_resultado.append(lista[j])
            i = j
        else:
            j += 1
    return lista_resultado 