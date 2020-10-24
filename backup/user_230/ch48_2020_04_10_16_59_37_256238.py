def eh_crescente(lista):
    if lista==[] or len(lista)==1:
        return True
    elif lista==sorted(lista):
        return True
    else:
        return False
       