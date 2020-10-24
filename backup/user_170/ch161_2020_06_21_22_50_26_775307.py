def PiWallis(n):
    produto = 2
    dividendo = 2
    divisor = 1
    produto = dividendo/divisor
    i = 1
    adcDendo = False
    adcDor = True
    while i < n:
        if adcDendo == True:
            dividendo += 2
        if adcDor == True:
            divisor +=2
        produto *= dividendo/divisor
        i =+ 1
    return produto