def calcula_euler(x,n):
    i = 1
    e = 1
    fatorial = 1
    while i<n and n>1:
        e = 1 + x + ((n-2)* ((x**i)/fatorial))
        i += 1
        fatorial = fatorial * (fatorial+1)
    return e