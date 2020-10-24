def imprime_tabuada(n):
    i = 1
    while i <= n:
        for valor in range(1, n+1):
            print(valor*i, end=' ')
        print('')
        i += 1