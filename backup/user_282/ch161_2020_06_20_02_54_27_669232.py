def PiWallis(n):
    valores = list()
    count = 1
    for i in range(1, n+1, 1):
        x = (2*i)/(2*i - 1)
        valores.append(x)
    for e in valores:
        count *= e
        
    return count*2