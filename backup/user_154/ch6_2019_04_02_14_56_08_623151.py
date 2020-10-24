def encontra_maximo(listas):
    result = 0
    for lista in listas:
        for x in lista:
            if x > 0:
                v = x
            else:
                v = -x
            if v > result:
                result = v
    return result