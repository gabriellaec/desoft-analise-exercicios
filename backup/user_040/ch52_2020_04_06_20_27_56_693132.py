def calcula_total_da_nota(a,b):
    lista = [0]
    x = -1
    if len(a) >= 0:
        for e in range(len(a)):
            while x < len(a):
                r = a[x+1]*b[x+1]
                lista[0] += r
                x += 1
        return lista
    else:
        lista.remove(0)
        return lista