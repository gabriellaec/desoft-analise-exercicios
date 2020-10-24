def lista_primos(n):
    t = 0
    primos = [2]
    num = 3
    while t <= n:
        i = 2
        if num % i != 0:
            i += 1
            while i < num:
                if num % i != 0:
                    i += 2
            primos.append(num)
        num += 1
        t += 1
    return primos