def primos_entre(a,b):
    p = a
    contador = 0
    while p <= b:
        if p == 0 or p == 1:
            p += 1
        elif p == 2 or p == 3:
            p += 1
            contador += 1
        elif p % 2 == 0:
            p += 1
        else:
            divisor = 3
            while divisor > p:
                if p % divisor == 0:
                    p += 1
                else:
                    d += 2
            contador += 1
            divisor = 3
            p += 1
    return contador
