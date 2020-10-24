def verifica_primos(num):
    dic = {}
    for n in num:
        for i in range(1, n+1):
            if n <= 0:
                dic[n] = False
            else:
                if n % i == 0:
                    dic[n] = True
                else:
                    dic[n] = False
    return dic
