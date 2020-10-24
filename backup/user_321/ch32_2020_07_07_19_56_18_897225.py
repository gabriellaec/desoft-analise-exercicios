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
                if b % d == 0 and b != d:
                    d += 2
                else:
                    print(b) 
        b += 1
        print(lis)
    return lis