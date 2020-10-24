def acha_bigramas(palavra):
    lista = []
    for i in range(2, len(palavra)+1):
        x = palavra[i-2: i]
        if x not in lista:
            lista.append(x)
    return lista