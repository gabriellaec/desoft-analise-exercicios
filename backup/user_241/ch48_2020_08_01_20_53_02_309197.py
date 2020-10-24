def eh_crescente(lista):
    if lista[0] > lista[1]:
        return False
    if lista[0] < lista[1]:
        return True
    if lista[0] == lista[1]:
        return False