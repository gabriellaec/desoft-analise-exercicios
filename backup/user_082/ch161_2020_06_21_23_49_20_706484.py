def PiWallis(n):
    num = 2
    den = 1
    sum = 1
    if n == 1:
        return 4.0
    else:
        for i in range(0,n):
            sum *= num/den
            if i % 2 == 0:
                den += 2
            else:
                num += 2
        return sum*2