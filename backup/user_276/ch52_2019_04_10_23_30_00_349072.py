def eh_crescente(lista):
    i = 0
    while i < len(lista):
        if lista[i + 1] > lista[i]:
            i += 1
        else:
            return 'False'
    return 'True'


lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(eh_crescente(lista1))
    