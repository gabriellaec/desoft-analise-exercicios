
def PiWallis(n):
    
    pi2 = 1
    
    c = 0

    for i in range(1, n + 1):
        l = (2.0 * i)/ (2.0 * i + (-1.0 ** i))
        
        pi2 = pi2 * l
    pi = pi2 * 2
        
    return pi
        