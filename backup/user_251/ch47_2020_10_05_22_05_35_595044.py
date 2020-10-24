i = 0
j = 0
def estritamente_crescente(lista):
    i = 0
    j = 0
    lista_resultado = []
    while i < len(lista)-1:
        if lista[i] < lista[j]:
            lista_resultado.append(lista[j])
            i = j
        else:
            j += 1
    return lista_resultado 