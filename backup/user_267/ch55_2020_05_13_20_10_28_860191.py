def encontra_maximo(m):
    maior = 0
    x = 0
    while x < len(m):
        for n in m[x]:
            modulo = abs(n)
            if modulo>maior:
                maior = n 
        x += 1
    return maior