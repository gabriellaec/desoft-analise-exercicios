def acha_bigramas(string):
    lista_bigramas = []
    contador = 0
    while contador < len(string):
        lista_bigramas.append(string[contador:contador+1:2])
        contador += 1
    return lista_bigramas