def acha_bigramas(x):
    lista = []
    t = 0
    while t < len(x) - 2:
        for i in range(t+1,len(x)):
            bigrama = x[t] + x[i]
            if bigrama not in lista:
                lista.append(bigrama)
        t += 1
    return lista