def eh_crescente(lista):
    if lista==[]:
        return False
    elif len(lista)<=1:
        return False
    elif lista[0]==lista[1]:
        return False
    elif lista==sorted(lista):
        return True
    else:
        return False
    