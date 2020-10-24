def eh_crescente(lista):
    for item in range(len(lista)):
        if lista==sorted(lista):
            return True
        else:
            return False
    