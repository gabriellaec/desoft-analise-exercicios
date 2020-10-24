def estritamente_crescente(lista):
    result = []
    
    i = 0
    
    while i < len(lista):
        
    
    test = True
    start = 0
    
    for x in lista:
        if test:
            test = False
            result.appned(x)
            start = x
            continue
        if x > start:
            result.appned(x)
            start = x
    
    return result