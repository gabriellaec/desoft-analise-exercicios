def verifica_primos(lista):
    d = {}
    for i in lista:
        if i < 2:
            i = False
        elif i == 2:
            i = True
        elif i%2 == 0:
            i = False
        else:
            if i % i == 0 and i%3 ==0 and i!=3 :
                i = False
            else:
                i = True
    return d