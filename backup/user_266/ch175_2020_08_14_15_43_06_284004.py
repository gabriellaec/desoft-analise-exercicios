def imprime_tabuada(n):
    m = 1
    for j in range(n):
        for i in range(1,n+1):
            print(i*m) if i == n else print(i*m, end=' ')
        m+=1