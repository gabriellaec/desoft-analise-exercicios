def imprime_tabuada (n):
    for i in range (n):
        b=i+1
        print(b,end=' ')
        y=b
        for ii in range (n-1):
            y+=b
            print(y,end=' ')