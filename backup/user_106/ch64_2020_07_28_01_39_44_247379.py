def acha_bigramas(texto):
    lista = []
    i = 0
    while i+1 < len(texto):
        lista.append(texto[i] + texto[i+1])
        i += 1
    return lista