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
            if i % i == 0 and i%3 ==0:
                d[i] = 'não'
            else:
                d[i] = 'primo'
    return d