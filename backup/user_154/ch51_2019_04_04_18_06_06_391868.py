def estritamente_crescente(lista):
    result = []
    
    start = 0
    
    for x in lista:
        if x > start:
            result.appned(x)
            start = x
    
    return result