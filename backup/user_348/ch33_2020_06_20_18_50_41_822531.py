def primos_entre (a,b):
    contador = 0
    p = 2
    while p >= a and p<=b:
        if p == 2:
            contador += 1
        for i in range (3, b, 2):
            if (p%2 !=0) and (p%i != 0):
                contador += 1
    return contador
    