def imprime_grade(n: int):
    for i in range(1, n+1):
        if i > 1:
            print("|" + " |"*n)
        for j in range(1, n+1):
            end = "-" if j < n else "-+\n"
            print("+", end=end)