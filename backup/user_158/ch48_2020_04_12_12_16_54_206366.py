def eh_crescente(lista):
    i=1
    while i < len(lista) and sub>0:
        sub = lista[1] - lista[i-1]
        return True
        i +=1
    return False
