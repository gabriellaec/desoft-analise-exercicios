def eh_crescente (lista):
    eh_crescente=True 
    i=1
    while i<len(lista):
        if lista[i]<=lista[i-1]:
            eh_crescente=False 
        i=i+1
    return eh_crescente