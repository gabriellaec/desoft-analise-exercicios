def encontra_maximo(listas):
    result = -99999999
    
    for lista in listas:
        for x in lista:
            if x > result:
                result = x
    
    return result