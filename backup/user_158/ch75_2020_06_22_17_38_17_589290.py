def  verifica_primos(lista):
    resp ={}
    for num in lista:
        i= 3
        if (num % 2) == 0 and num != 2 and num <=1:
            resp[num] = False
        while num > i:
            if (num % i) == 0:
                resp[num] = False
            i += 2
        resp[num] = True
    return resp