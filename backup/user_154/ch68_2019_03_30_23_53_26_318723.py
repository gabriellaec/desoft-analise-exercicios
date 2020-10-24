def separa_trios(lista):
    result = []
    
    preresult = []
    
    for x in lista:
        if len(preresult) == 3:
            result.append(preresult)
            preresult = []
        preresult.append(x)
    return result