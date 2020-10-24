def eh_crescente(lista):
    for item in lista:
        if lista==sorted(lista):
            return True
        else:
            return False
    