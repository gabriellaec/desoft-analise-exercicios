def PiWallis(num):
    pi = 0
    for n in num:
        if n%2 == 0:
            pi = pi*(n+2)/(n+1)
        elif n%2 == 1:
            pi = pi*(n+1)/(n+2)
    return pi*2