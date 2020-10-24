def calcula_total_da_nota(a, b):
    lista = []
    i = 0
    while i < len(b):
        lista.append(a[i] * b[i])
        i += 1
    return sum(lista)