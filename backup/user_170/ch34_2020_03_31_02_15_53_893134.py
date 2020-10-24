def maior_primo_menor_que(n):
    primos = []
    t = 0
    while t <= n:
        ehPrimo = True
        if t == 0 or t == 1:
            ehPrimo = False
        if t%2==0 and t!=2:
            ehPrimo = False
        else:
            i = 3
            while i < t:
                if t%i==0:
                    ehPrimo = False
                i += 2
        if ehPrimo == True:
            primos.append(t)
        t += 1
    if len(primos) == 0:
        return -1
    else:
        return primos[-1]

print(maior_primo_menor_que(-10))