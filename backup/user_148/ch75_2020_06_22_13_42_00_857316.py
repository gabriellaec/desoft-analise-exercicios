def verifica_primos(num):
    dic = {}
    for i in num:
        for p in range(1, i+1):
            if i>0:
                if i % p == 0:
                    dic[i] = True
                else:
                    dic[i] = False
                x += 1
                