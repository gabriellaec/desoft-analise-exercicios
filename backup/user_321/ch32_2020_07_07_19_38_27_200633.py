def lista_primos(n):
    lis = []
    b = 2
    i = 2
    d = 3
    if n == 1:
        lis.append(b)
    while i <= n:
        if b % 2 != int:
            while d < b:
                if b % d == 1:
                    lis.append(b)
                    i += 1
                else:
                    d += 2 
        print(b)
        b += 1
        print(b)
    return lis

print(lista_primos(2))