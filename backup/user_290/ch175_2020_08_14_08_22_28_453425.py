def imprime_tabuada(n):
    for i in range(0, n + 1):
        for j in range(1, n + 1):
            print(i * j, end=' ')
        print()