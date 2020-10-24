def encontra_maximo(m):
    maior = 0
    lista = []
    x = 0
    while x <= len(m):
        a = 0
        i = 0
        for n in m[i]:
            lista.append(n)
            x += 1
            i += 1
            if n>maior:
                maior = n           
    return maior