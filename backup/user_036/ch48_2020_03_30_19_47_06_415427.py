def eh_crescente(lista):
    print(lista)
    if lista == sorted(lista):
        return True
    elif lista[0] == lista[1]:
        return False
    else:
        return False