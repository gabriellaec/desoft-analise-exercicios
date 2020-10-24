def conta_a(p):
    s = 0
    lista = list(p)
    n = len(lista)
    i = 0
    while i < n:
        if lista[i] == 'a':
            s += 1
        i += 1
    print(s)

