def eh_crescente (lista):
    for x in lista:
        if lista == sorted(lista):
            return True
        else:
            return False