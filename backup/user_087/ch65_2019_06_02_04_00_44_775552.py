def acha_bigramas(palavra):
    lista = []
    i = 0
    while i < len(palavra):
        lista.append(palavra[i:i+2])
        i += 1
    return lista
