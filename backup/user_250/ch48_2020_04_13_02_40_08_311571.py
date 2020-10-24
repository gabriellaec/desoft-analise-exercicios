def eh_crescente(lista):
    i = 1
    if lista == [] or len(lista) == 1:
        return True
    while i < len(lista)-1:
        if lista [i] <= lista [i-1]:
            return False
        else:
            return True