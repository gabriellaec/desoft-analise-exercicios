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
            adcDor = True
            adcDendo = False
        elif adcDor == True:
            divisor += 2
            adcDor = False
            adcDendo = True
        produto *= dividendo/divisor
        i += 1
    produto *= 2
    return produto