def verifica_primos(lista):
    dic = {}
    for e in lista:
        if e < 0:
            e_neg = e
            e *= -1
            num = 2
            menores = []
            while num < e:
                menores.append(num)
                num += 1
            if e < 2:
                dic[e_neg] = False
            elif e == 2:
                dic[e_neg] = True
            elif e % 2 == 0:
                dic[e_neg] = False
            else:
                for i, n in enumerate(menores):
                    if e % n ==0:
                        menores[i] = False
                    else:
                        menores[i] = True
                if False in menores:
                    dic[e_neg] = False
                else:
                    dic[e_neg] = True
        else:
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
                for i, n in enumerate(menores):
                    if e % n ==0:
                        menores[i] = False
                    else:
                        menores[i] = True
                if False in menores:
                    dic[e] = False
                else:
                    dic[e] = True
    return dic