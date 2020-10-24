def acha_bigramas(palavra):
    contador = 0
    lista = []
    for i in range(0,len(palavra),2):
        if i in lista:
            pass
        else:
            lista.append(i)   
    return lista
        