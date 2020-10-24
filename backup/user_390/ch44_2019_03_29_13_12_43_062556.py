def soma_valores(lista):
    i=0
    s=0
    while i<len(lista)+1:
        lista[i+2]=lista[i]+lista[i+1]
        s=lista[i+2]+s
        i+=2
    return s
