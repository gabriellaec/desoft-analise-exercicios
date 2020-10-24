def eh_cresecente(lista):
    i=0
    while i<len(lista):
        if lista[i+1]>lista[i]:
        i=i+1
        return True
        else:
            False