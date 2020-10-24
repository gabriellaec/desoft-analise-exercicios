def separa_trios(lista):
    result = []
    
    trio = []
    
    for x in lista:
        if len(trio) == 3:
            result.append(trio)
            trio = []
        trio.append(x)
    return result