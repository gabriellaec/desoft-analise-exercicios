def verifica_primos(lista):
    d = {}
    for i in lista:
        if i < 2:
            d[i] = False
        elif i == 2:
            d[i] = True
        elif i%2 == 0:
            d[i] = False
        else:
            if i % i == 0 and i%3 ==0 and i!=3 :
                d[i] = False
            else:
                d[i] = True
    return d