def eh_crescente(lista):
    if len(lista)==1 or lista==[]:
        retunr True
    for i in range(len(lista)-1):
        if lista[i+1]<=lista[i]:
            return False
    return True
