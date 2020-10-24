def separa_trios(lista):
    result = []  
    trio = []
    
    for x in lista:
        trio.append(x)
        if len(trio) == 3:
            result.append(trio)
            trio = []
        
    return result