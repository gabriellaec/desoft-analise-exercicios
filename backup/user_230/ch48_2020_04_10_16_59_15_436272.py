def eh_crescente(lista):
    for i in range(len(lista)):
        if lista[i]==lista[i+1]:
            return False
    if lista==[] or len(lista)==1:
        return True
    elif lista==sorted(lista):
        return True
    else:
        return False
       