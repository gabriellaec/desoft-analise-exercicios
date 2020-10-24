
def PiWallis(n):
    
    pi2 = 0
    
    if n == 1:
        return 4
    
    for i in range(n):
        l = (2 * i)/ (2 * 1 - 1)
        r = (2 * i)/ (2 * 1 + 1)
        t = l * r
        pi2 += (t)
    
    return pi2 * 2