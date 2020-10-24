def lista_primos(n):
    lis = []
    b = 2
    i = 2
    d = 3
    if n == 1:
        lis.append(b)
    while i <= n:
        print(b)
        if b % 2 != 0:
            print('nao e divisivel p 2')
            while d <= b:
                if b % d == 0 and b == d:
                    lis.append(b)
                    i += 1
                else:
                    d += 2 
        b += 1
    return lis