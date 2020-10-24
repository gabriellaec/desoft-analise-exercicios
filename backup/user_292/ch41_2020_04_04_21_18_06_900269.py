def zera_negativos(T):
    lista = []
    a = len(T)
    x = 0
    while x< a:
        if T[x]>=0:
            lista.append(T[x])
        elif T[x] < 0:
            r = 0
            lista.append(r)
        x+=1
    return lista