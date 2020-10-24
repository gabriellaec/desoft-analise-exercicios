def eh_crescente(lista):
    print(lista)
    if lista[0]==lista[1]:
        return False
    if lista==sorted(lista):
        return True
    else:
        return False
    