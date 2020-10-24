def eh_crescente(lista):
    i = 0
    while i < len(lista)-1:
        max = lista[0]
        if lista[i] > max:
            return True
        else:
            return False