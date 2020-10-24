def encontra_maximo(listas):
    result = 0
    test = True
    
    for lista in listas:
        for x in lista:
            if test:
                result = x
                test = False
                continue
            if x > result:
                result = x
    
    return result