def verifica_primos(lista):
    d = {}
    for i in lista:
        if i < 2:
            d[i] = 'não'
        elif i == 2:
            d[i] = 'primo'
        elif i%2 == 0:
            d[i] = 'não'
        else:
            n = 3
            while i%n!=0:
                n+=2
            if i == n:
                d[i] = 'primo'
    return d