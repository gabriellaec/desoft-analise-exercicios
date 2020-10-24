def verifica_primos(lista):
    d = {}
    for i in lista:
        if i < 2:
            d['não'] = i
        elif i == 2:
            d['primo'] = i
        elif i%2 == 0:
            d['não'] = i
        else:
            if i % i == 0 and i%3 ==0 and i!=3 :
                d['não'] = i
            else:
                d['primo'] = i
    return d