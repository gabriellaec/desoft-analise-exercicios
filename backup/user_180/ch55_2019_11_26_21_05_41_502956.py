def primos_entre(a, b):
    lista_primos = []
    for i in range(a, b+1):
        if i == 0 or i == 1:
            pass
        elif i == 2:
            lista_primos.append(i)
        elif n % 2 == 0:
            pass
        else:
            x = 3
            while x < i:
                if i % x == 0:
                    pass
                x = x + 2
            if x == i:
                lista_primos.append(i)
            else:
                pass
    return lista_primos