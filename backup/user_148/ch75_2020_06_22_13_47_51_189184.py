def verifica_primos(num):
    dic = {}
    i = 1
    for n in num:
        if n>0:
            while i<n:
                if n % i == 0:
                    dic[n] = True
                else:
                    dic[n] = False
                i += 1
                