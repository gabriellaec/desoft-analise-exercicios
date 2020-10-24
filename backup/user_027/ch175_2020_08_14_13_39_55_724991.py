def imprime_tabuada(n: int):

    for i in range(1, n+1):
        for j in range(1, n+1):
            end = " " if j < n else "\n"
            print(i*j, end=end)