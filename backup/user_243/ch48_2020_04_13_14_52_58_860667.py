def eh_crescente(lista):
    if lista==[] or len(lista)==1:
        return True
    i=0
    while len(lista)-1>i:
        if lista[i+1]<=lista[i]:
            return False
    i+=1
    return True
    