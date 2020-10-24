def PiWallis(n):
    num = 2
    den = 1
    sum = 1
    if n == 1:
        return 4.0
    else:
        for i in range(0,n+1):
            sum *= num/dem
            if i % 2 == 0:
                dem += 2
            else:
                nem += 2
        return sum*2