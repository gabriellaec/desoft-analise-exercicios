def primos_entre(a, b):
    p = 0
    for e in range(a, b+1):
        if e == 2:
            p += 1
        else:
            if e != 0 and 1:
                contador = 2
                while contador < e:
                    if numero%contador != 0:
                        contador += 1
                p += 1        