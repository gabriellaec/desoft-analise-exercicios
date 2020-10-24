def eh_crescente(lista):
    if lista[0]==lista[1]:
        return False
    elif lista==[] or len(lista)==1:
        return True
    elif lista==sorted(lista):
        return True
    else:
        return False
       