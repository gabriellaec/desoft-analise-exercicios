def encontra_maximo(m):
    maior = 0
    x = 0
    i = 0
    while x <= len(m):
        for n in m[i]:
            if n>maior:
                maior = n 
        i += 1
        x += 1
    return maior