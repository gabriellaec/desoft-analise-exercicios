def lista_primos(n):
    lis = []
    b = 2
    i = 2
    d = 3
    if n != 0:
        lis.append(b)
    while i <= n:
        if b % 2 != 0:
            while d <= b:
                if b % d == 0:
                    if b != d:
                        d += 2
                    else:
                        lis.append(b)
                        break
        b += 1
        print(lis)
    return lis