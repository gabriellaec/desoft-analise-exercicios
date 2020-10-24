def calcula_total_da_nota(a,b):
    lista = [0]
    if len(a) > 0:
        x = 1
        while x < len(a)+1:
            r = a[x]*b[x]
            lista[0] += r
            x += 1
        return lista
    else:
        return [0]