def calcula_total_da_nota(a,b):
    lista = [0]
    x = 0
    if len(a) > 0:
        for e in range(len(a)):
            while x < len(a):
                r = a[x]*b[x]
                lista[0] += r
                x += 1
        return lista
    else:
        return [0]