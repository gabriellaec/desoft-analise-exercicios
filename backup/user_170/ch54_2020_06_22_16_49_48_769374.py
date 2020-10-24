def calcula_fibonacci(n):
    liFi = [0]*n
    liFi[0] = [1]
    liFi[1] = [1]
    
    for i in range(3, n):
        liFi[i] = liFi[i-1]+liFi[i-2]
    return liFi[-1]
                