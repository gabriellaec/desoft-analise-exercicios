def PiWallis(n):
    numerador=2
    denominador=1
    x=1
    i=1
    if n <= 1:
        return 4
    while i <= n:
        x*=numerador/denominador
        print(f'{numerador}/{denominador}')
        if numerador/denominador > 1:
            denominador += 2
        else:
            numerador += 2
        i+=1
    return 2*x
n = 9
q=PiWallis(n)
print(q)