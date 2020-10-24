def encontra_maximo(listas):
    result = -sys.maxint-1
    
    for lista in listas:
        for x in lista:
            if x > result:
                result = x
    
    return result