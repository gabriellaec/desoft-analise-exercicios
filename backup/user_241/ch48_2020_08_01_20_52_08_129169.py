i = 0
def eh_crescente(lista):
    if lista[i] > lista[i+1]:
        return False
    if lista[i] < lista[i+1]:
        return True
    if lista[i] == lista[i+1]:
        return False