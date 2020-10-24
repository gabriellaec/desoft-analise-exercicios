def imprime_tabuada(n):
    x = 1
    for e in range(0,n):
        c = 1
        sf = ""
        for i in range(0,n):
            result = x*c
            sf += str(result) + " "
            c += 1
        print(sf)
        x += 1