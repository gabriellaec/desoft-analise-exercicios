def acha_bigramas(string):
    lista = []
    for i in range(2, len(string)+1):
        f = string[i-2:i] #fatiando
        if f not in lista:
            lista.append(f)
    return lista