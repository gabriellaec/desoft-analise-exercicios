def PiWallis(n):
    numerador=2
    denominador=1
    x=1
    i=1
    while i < n:
        x*=numerador/denominador
        if numerador/denominador > 1:
            denominador += 2
        else:
            numerador += 2
        i+=1
    return x
n = 3
q=PiWallis(n)
print(q)