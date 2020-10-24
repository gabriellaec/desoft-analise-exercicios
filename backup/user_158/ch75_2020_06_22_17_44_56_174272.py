def  verifica_primos(lista):
    resp ={}
    for num in range(0,len(lista)):
        i= 3
        if (lista[num] % 2) == 0 and lista[num] != 2 and lista[num] <=1:
            resp[lista[num]] = False
        while lista[num] > i:
            if (lista[num] % i) == 0:
                resp[lista[num]] = False
            i += 2
        resp[lista[num]] = True
    return resp