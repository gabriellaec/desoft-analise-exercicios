def calcula_total_da_nota(lista, lista2):
    i = 0
    s = 0
    while i<len(lista):
        s += lista[i] * lista2[i]
        i+=1
    return s
        