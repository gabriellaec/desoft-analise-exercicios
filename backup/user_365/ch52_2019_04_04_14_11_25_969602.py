def eh_crescente(lista):
    i=1
    o=0
    while i<len(lista[i]):
        if lista[i]>lista[o]:
            i+=1
            o+=1
            return True
        else:
            return False
        