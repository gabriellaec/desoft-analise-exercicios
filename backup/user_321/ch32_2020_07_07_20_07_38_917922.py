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
                    print("b: {0}".format(b))
                    print("d: {0}".format(d))
                    if b != d:
                        d += 2
                    else:
                        print("entrou")
                        lis.append(b)
                        i += 1
                        print("i: {0}".format(i))
                        break
        else: b += 1
    print(lis)
    return lis