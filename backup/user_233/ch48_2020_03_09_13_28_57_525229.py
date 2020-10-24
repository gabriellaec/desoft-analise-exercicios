def eh_crescente(lista):
    
    if len(lista) == 0: return True
    
    last = lista[0]
    
    for i in lista[1:]:
        if i <= last: return False
        last = i
    
    return True