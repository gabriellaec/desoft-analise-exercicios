def imprime_tabuada(n):
    x = 1
    for e in range(0,n):
        c = 1
        for i in range(0,n):
            result = x*c
            print("result", end='')
            c += 1
        x += 1