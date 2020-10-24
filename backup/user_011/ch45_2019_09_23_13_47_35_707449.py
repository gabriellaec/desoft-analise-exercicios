def zera_negativos(lista_n):
    lista_0_neg = []
    for n in lista_n:
        if n < 0:
            n = 0
            lista_0_neg.append(n)
        else:
            lista_0_neg.append(n)