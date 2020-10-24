def eh_crescente(lista):
    i = 0
    while i < range(len(lista)):
        if lista[i] <= lista[i+1]:
            return True
        else:
            return False