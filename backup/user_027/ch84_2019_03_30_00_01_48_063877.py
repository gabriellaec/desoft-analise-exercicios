def inverte_dicionario(x):
    lista_reserva = {}
    for i in x:
        if x[i] not in lista_reserva:
            lista_reserva[x[i]] = [i]
        else:
            lista_reserva[x[i]].append(i)
        
    return lista_reserva
