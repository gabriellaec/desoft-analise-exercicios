
def PiWallis(n):
    
    pi2 = 0
    
    c = 0

    for i in range(n):
        l = (2 * i)/ (2 * i - 1)
        c += 1
        if n > c:
            r = (2 * i)/ (2 * i + 1)
            t = l * r
        else:
            t = l
        pi2 += (t)
    
    return pi2 * 2