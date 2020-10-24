def lista_primos(n):
    lis = []
    b = 2
    i = 2
    d = 3
    if n == 1:
        lis.append(b)
    while i <= n:
        print(b)
        if b % 2 != int:
        print('nao e divisivel p 2')
            while d < b:
                if b % d == 1:
                    print(d,b)
                    lis.append(b)
                    i += 1
                else:
                    d += 2 
        b += 1
    return lis

print(lista_primos(2))