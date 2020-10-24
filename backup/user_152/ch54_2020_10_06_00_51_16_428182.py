def calcula_fibonacci(n):
    fibo = []
    if n>0:
        if n == 1:
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
            while i<n:
                fibo.append(fibo[i-1]+fibo[i-2])
                i += 1
            return fibo