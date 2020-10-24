def imprime_tabuada(n):
    x = 1
    for e in range(0,n):
        c = 1
        for i in range(0,n):   
            print(x*c, end='')
            print(" ", end='')
            c += 1
        print("\n")
        x += 1