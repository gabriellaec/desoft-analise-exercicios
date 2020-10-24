def verifica_primos(lista):
    d = {}
    for i in range(len(lista)):
        if lista[i] < 2:
            d[i] = 'não'
        elif lista[i] == 2:
            d[i] = 'primo'
        elif lista[i]%2 == 0:
            d[i] = 'não'
        else:
            n = 3
            while lista[i]%n!=0:
                n+=2
            if lista[i] == n:
                d[i] = 'primo'
    return d