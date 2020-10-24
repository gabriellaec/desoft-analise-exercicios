def PiWallis(n):
    pi = 1
    for i in range(1,n):
        if n%2 == 1:
            numerador = n + 1
            denominador = n
        elif n%2 == 0:
            numerador = n
            denominador = n + 1  
        pi *= numerador/denominador
    return pi*2

print(PiWallis(10))