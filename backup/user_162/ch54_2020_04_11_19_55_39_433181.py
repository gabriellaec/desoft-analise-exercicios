def calcula_fibonacci(n):
    if n >= 2:
        lsfib = [1, 1]
        i = 0
        while i < n - 2:
            lsfib.append(lsfib[i] + lsfib[-1])
            i+=1
        return lsfib
    else:
        if n == 1 :
            lsfib = [1]
            return lsfib
        else:
            lsfib = []
            return lsfib