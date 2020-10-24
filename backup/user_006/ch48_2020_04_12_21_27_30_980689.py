def eh_crescente(lista):
    v=True
    i=1
    while i<len(lista) and v==True:
        if lista[i-1]<lista[i]:
            i=i+1
        else:
            v=False
    if v==False:
        return False
    if v==True:
        return True