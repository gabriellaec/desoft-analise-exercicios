def imprime_grade(n):
    x = n+1
    cond = True
    for i in range(x):
        if cond == True:
            print("+-"*n+"+")
            cond = False
        if not i == x-1:
            print("| "*n+"|")
        cond = True