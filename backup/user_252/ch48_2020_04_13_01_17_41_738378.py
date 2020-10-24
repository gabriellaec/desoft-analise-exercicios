def eh_cresecente(lista):
    i=0
    while i<len(lista):
        if lista[i-1]<lista[i]:
            i+=1
        else:
            return False
    return True