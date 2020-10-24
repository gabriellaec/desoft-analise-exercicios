def junta_listas(listas):
    result = []
    
    for x in listas:
        for y in x:
            result.append(y)
    return result