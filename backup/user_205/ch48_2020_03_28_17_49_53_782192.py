def eh_crescente(lista):
    for i in range(len(lista)):
        if lista==sorted(lista):
            return True
        else:
            return False
    