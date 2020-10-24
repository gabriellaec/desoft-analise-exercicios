def calcula_fibonacci(n):
    fibo = []
    if n == 0:
        return fibo
    elif n == 1:
        fibo.append(1)
        return fibo
    elif n == 2:
        fibo.append(1)
        fibo.append(1)
        return fibo
    else:
        fibo.append(1)
        fibo.append(1)
        i = 2
        f1 = 1
        f2 = 1
        f = 0
        while i < n:
            f = f1 + f2
            f2 = f1
            f1 = f
            fibo.append(f)
            i += 1
        return fibo