def eh_crescente (lista):
    eh_crescente1=True 
    i=1
    while i<len(lista):
        if lista[i]<lista[i-1]:
            eh_crescente1=False 
        i=i+1
    return eh_crescente1