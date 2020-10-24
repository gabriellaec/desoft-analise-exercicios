def acha_bigramas(palavra):
    lista = []
    for i in range(len(palavra)):
        if i+2 <= len(palavra):
            lista.append(palavra[i:i+2])
    return lista 