def eh_crescente(lista):
    print(lista)
    if lista[0]==lista[1] or len(lista)<=2:
        return False
    elif lista==sorted(lista):
        return True
    else:
        return True
    