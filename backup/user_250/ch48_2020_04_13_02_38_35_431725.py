def eh_crescente(lista):
    i = 1
    if lista == [] or len(lista) == 1:
        return True
    while i < len(lista)-1:
        max = lista[0]
        if lista[i] > max:
            return True
            i = i+1
        else:
            return False