def calcula_fibonacci(n):
    liFi = []
    liFi.append(1)
    liFi.append(1)
    if n == 1:
        return 1
    if n == 2:
        return 1
    for i in range(1, n):
        liFi.append(liFi[i-1]+liFi[i-2])
    return liFi[-1]