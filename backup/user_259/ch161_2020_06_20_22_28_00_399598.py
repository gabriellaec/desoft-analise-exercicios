def PiWallis(n):
    x = 1
    pi = 1
    for i in range(1,n):
        if x == 1:
            numerador = n + x
            denominador = n
            x += 1
        elif x == 2:
            numerador = n
            denominador = n + x
            x = 1
        pi *= numerador/denominador
    return pi*2

print(PiWallis(10))