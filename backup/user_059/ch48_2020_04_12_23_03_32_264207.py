def eh_crescente(lista):
    i=0
    while i<len(lista)-1:
        if lista[i+1] > lista[i]:
            pass
        if i == len(lista)-2:
            return True
        else:
            return False
        i+=1
        