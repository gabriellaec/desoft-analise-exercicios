def eh_crescente(lista):
    i=1
    a=True
    while i<len(lista):
        if lista[i-1]<lista[i]:
            i+=1
        else:
            a=False
    return a         
        
        