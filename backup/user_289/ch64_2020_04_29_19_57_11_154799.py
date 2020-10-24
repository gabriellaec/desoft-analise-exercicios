def acha_bigramas(palavra):
    lista = []
    i = 0
    while i < len(palavra):
        bigrama = palavra[i] + palavra[i+1]
        lista.append(bigrama)
        i += 1
    return lista