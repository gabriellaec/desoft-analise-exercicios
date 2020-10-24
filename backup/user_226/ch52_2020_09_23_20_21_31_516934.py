def calcula_nota_fiscal(a, b):
    lista = []
    i = 0
    while i < len(b):
        lista.append(a[i] * b[i])
        i += 1
    return sum(lista)