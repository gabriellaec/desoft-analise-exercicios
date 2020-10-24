def eh_crescente(lista):
    i=1
    c=True
    while i<len(lista):
        if lista[i]<=lista[i-1]:
            c=False
            return c
            i==len(lista)
        i+=1
    if c==False:
        return False
    else:
        return True