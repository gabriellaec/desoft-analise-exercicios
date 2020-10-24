def PiWallis(x):
    dividendo = 2
    divisor = 1
    pi = 1
    for i in range(1, x + 1):
        pi *= dividendo/divisor
        if i % 2 != 0:
            divisor += 2
        else:
            dividendo += 2
            
    return pi*2