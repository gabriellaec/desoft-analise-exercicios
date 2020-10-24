def lista_primos(n):
    primos = [0]*n
    i = 2
    primos[0] = 2
    if n > 0:
        primos[1] = 3
        while i < n:
            x = 3
            while x < primos[i-1]:
                if (primos[i-1]+2)%x != 0:
                    x += 2
                    primos[i] = primos[i-2] + 2
                else:
                    i += 1
                    x += 2
            else:
                x += 2
    print(primos)