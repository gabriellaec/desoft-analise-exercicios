def estritamente_crescente(lista):
    lista_filtrada = filter(lambda item: item >= lista[0],lista)
    return sorted(list(dict.fromkeys(lista_filtrada)))

