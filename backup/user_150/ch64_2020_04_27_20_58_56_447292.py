def acha_bigramas(string):
    lista_bigramas = []
    i = 1
    for letras in string:
        bigrama = string[:i]
        lista_bigramas.append(bigrama)
        i += 2
    return lista_bigramas