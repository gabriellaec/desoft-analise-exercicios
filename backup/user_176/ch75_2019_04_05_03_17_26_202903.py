def verifica_primos(L):
    dic = {}
    i = 0
    L[i] = int(L[i])
    while i < len(L):
        divisor = 2
        primo = True
        if L[i] < 2:
            dic[L[i]] = False
        elif L[i] == 2:
            dic[L[i]] = True
        else:
            while divisor < L[i]:
                if L[i] % divisor == 0:
                    primo = False
                divisor += 1
            dic[L[i]] = primo
        i += 1
    return dic