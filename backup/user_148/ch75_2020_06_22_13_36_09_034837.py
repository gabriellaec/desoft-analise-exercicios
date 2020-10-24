def verifica_primos(num):
    dic = {}
    x = 1
    for i in num:
        if i > 0:
            if i % x == 0:
                dic[i] = True
            else:
                dic[i] = False
            x += 1