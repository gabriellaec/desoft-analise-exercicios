def eh_crescente(lista):
    i = 0
    if len(lista) == 0:
        return True
    elif len(lista) == 1:
        return True
    
    while i < len(lista)-1:
       
        if lista[i+1] <= lista[i]:
            return False
        i += 1 
        
    return True
    