def maior_primo_menor_que.(n):
    if n<2:
        return '-1'
    primos = []
    for i in range(2,n+1):
        if i==2:
            primos += [i]
        else:
            d=3
            while i%d!=0 and i>d:
                d=d+2
            if i==d:
                primos += [i]
    maiorP = 0
    for i in primos:
        if i >maiorP:
            maiorP = i
    return maiorP