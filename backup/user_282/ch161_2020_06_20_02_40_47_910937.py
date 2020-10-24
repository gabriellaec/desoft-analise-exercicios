def PiWallis(n):
    valores = list()
    product = list()
    count = 1
    for i in range(1, n+1, 1):
        x = (4*(i**2))/(4*(i**2) - 1)
        valores.append(x)
    for e in valores:
        count *= e
        
    return count*2