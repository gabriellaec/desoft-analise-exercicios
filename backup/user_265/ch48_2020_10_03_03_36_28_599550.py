def eh_crescente(lista):
    i = 1
    while i < len(lista):
        i += 1
        if lista[i] < lista[i+1]:
            return True
        elif lista[i] == lista[i+1]:
            return False
        else:
            return False