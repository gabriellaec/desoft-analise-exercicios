def maior_primo_menor_que(n):
    primos = []
    k = 0
    while len(primos) < n:
        Primos = True
        if k == 0 or k == 1:
            Primo = False
        if k%2 == 0 and k != 2:
            Primo = False
        else:
            i = 3
            while i < k:
                if k%i == 0:
                    Primo = False
                i = i+2
        if Primo == True:
            primos.append(k)
        k = k+1
    maior = primos[len(primos-1)]
    return maior