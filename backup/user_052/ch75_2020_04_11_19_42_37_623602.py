def verifica_primos (lista):
    dic = {}
    for n in lista:
        if n == -1 or n == 0 or n == 1:
            dic[n] = False
        elif n == 2:
            dic[n] = True
        else:
            dic[n] = True
            if n%2 == 0:
                dic[n] = False
            else:
                i = 3
                while n > i:
                    if n%i == 0:
                        dic[n] = False
                        i += 2
                    else: 
                        i += 2
    return dic          