def calcula_total_da_nota(a,b):
    lista = []
    x = 0
    while x <= len(a):
        r = a[x]*b[x]
        lista.append(r)
        x += 1
        return lista