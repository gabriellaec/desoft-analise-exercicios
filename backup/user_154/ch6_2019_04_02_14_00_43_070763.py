def encontra_maximo(listas):
    result = 0
    
    for lista in listas:
        for x in lista:
            if x > result:
                result = x
    
    return result