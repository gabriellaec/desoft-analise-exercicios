def conta_a(n):
    contador = 0
    i = 0
    x = len(n)
    while i < x:
        if n[i]=='a':
            contador += 1
        i += 1
    return contador