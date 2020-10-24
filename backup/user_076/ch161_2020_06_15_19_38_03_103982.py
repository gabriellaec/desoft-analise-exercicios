def PiWallis(n):
    numerador = 2
    denominador = 1
    valor = 1
    c=0
    while c<n:
        valor*=numerador/denominador
        if c%2==0:
            denominador += 2
        else:
            numerador += 2
        c+=1
    return 2*valor
            