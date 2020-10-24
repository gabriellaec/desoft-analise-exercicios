def verifica_primos (lista):
    dic = {}
    for n in lista:
        if n == 1 or n == 2 or n == 3:
            dic[n] = True
        elif n <= 0:
            dic[n] = False
        i = 2
        while n > 3 and i <= len(lista):
            if n%i == 0:
                dic[n] = False
            else:
                dic[n] = True
            i += 1
    return dic   