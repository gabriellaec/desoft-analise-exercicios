def verifica_primos(num):
    dic = {}
    x = 1
    for i in num:
        if i % x == 0:
            dic[i] = True
            x += 1
        else:
            dic[i] = False
                