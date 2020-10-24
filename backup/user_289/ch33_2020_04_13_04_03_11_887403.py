def primos_entre(a, b):
    p = 0
    for e in range(a, b+1):
        if e == 2:
            p += 1
        elif e == 3:
            p += 1
        else:
            if e != 0 and 1:
                contador = 2
                for n in range e:
                    if e%n != 0:
                        contador += 1
                p += 1
    return p