def acha_bigramas(palavra):
    contador = 0
    lista = []
    for i in range(0,len(palavra)):
        if palavra[i:i+2] in lista:
            pass
        else:
            lista.append(i)   
    return lista
        