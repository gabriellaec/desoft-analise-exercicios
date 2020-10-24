def separa_trios(lista):
    result = []  
    trio = []
    
    for x in lista:
        trio.append(x)
        if len(trio) == 3:
            result.append(trio)
            trio = []
    if len(trio) != 0:
        result.append(trio)
    return result