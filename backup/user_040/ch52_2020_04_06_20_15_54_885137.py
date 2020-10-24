def calcula_nota_fiscal(a,b):
    lista = []
    x = 0
    while x < len(a):
        r = a[x]*b[x]
        lista.append(r)
        x += 1