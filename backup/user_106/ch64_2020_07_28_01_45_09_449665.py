def acha_bigramas(texto):
    lista = []
    i = 0
    while i+1 < len(texto):
        bigrama = texto[i] + texto[i+1]
        if not bigrama in lista:
            lista.append(bigrama)
        i += 1
    return lista
    