def encontra_maximo(listas):
    result = -2**31-1
    
    for lista in listas:
        for x in lista:
            if x > result:
                result = x
    
    return result