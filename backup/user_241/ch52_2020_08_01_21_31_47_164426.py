def calcula_total_da_nota(lista1,lista2):
    x = 0
    i = 0
    while i < len(lista1):
        x += lista1[i] * lista2[i]
        i += 1
    return x
    