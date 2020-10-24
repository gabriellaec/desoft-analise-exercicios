def calcula_total_da_nota(a, b):
    lista = []
    for i in range (0, len(a)):
        c = a[i] * b[i]
        lista.append(c)
    total = sum(lista)
    return total