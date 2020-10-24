def lista_primos(n):
    lis = []
    b = 2
    i = 1
    d = 3
    if n != 0:
        lis.append(b)
    while i < n:
        print("i: {0}".format(i))
        if b % 2 != 0:
            while d <= b:
                if b % d == 0:
                    print("b: {0}".format(b))
                    print("d: {0}".format(d))
                    if b != d:
                        d += 2
                        b += 1
                    else:
                        print("entrou")
                        lis.append(b)
                        i += 1
                        b += 1
                        break
                else:
                    d += 2
        else: 
            print("b + 1 pq era divisivel por dois")
            b += 1
    print(lis)
    return lis