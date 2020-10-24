def verifica_primos(lista):
    dic = {}
    for i in lista:
        count = 0
        mult = 0
        while mult <= i or count < 2:
            mult += 1
            p = i % mult
            if p == 0:
                count += 1
            if count <= 2:
                dic[i] = True
        else:
            dic[i] = False
    return dic