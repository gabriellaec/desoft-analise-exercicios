def eh_crescente(lista):
    while i < len(lista):
        if lista[i + 1] > lista[i]:
            return 'True'
        else:
            return 'False'
    