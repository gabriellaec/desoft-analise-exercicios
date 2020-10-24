def verifica_primos (lista):
    dic = {}
    for n in lista:
        if n == 1 or n == 2 or n == 3:
            dic[n] = True
        i = 0
        while n > 3:
            if n%i == 0:
                dic[n] = False
            else:
                dic[n] = True
            i += 1
    return dic
            
            