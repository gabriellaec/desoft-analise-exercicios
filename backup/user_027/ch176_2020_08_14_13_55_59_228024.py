def imprime_grade(n: int):
    for i in range(n+1):
        print("+" + '-+'*(n))
        if i < n:
            print("|" + " |"*n) 