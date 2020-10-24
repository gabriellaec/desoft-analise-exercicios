def eh_crescente(lista):
    i = 0
    while i < len(lista)-1:
        i += 1
        if lista[i] < lista[i+1]:
            return True
        elif lista[i-1] == lista[i]:
            return False
        else:
            return False