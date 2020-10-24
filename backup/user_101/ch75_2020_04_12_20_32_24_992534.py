def verifica_primos(lista):
    dic = {}
    for e in lista:
        if e < 0:
            e *= -1
        num = 2
        menores = []
        while num < e:
            menores.append(num)
            num += 1
        if e < 2:
            dic[e] = False
        elif e == 2:
            dic[e] = True
        elif e % 2 == 0:
            dic[e] = False
        else:
            for n in menores:
                if e % n ==0:
                    n = False
                else:
                    n = True
            if False in menores:
                dic[e] = False
            else:
                dic[e] = True
    return dic