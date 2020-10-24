def lista_primos(n):
    lis = []
    b = 2
    i = 1
    d = 3
    while i <= n:
        if b % 2 != int:
            while d < b:
                if b % d == 1:
                    lis.append(b)
                    print(b)
                    i += 1
                else:
                    d += 2 
        b += 1
    lis.append(b)
    return lis