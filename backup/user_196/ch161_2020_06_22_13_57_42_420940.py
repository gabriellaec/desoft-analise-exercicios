def PiWallis(n):
    metadedepi = 1
    for i in range (1,n+1):
        if i%2 == 0:
            numero = (i)/(i+1)
        elif i%2 != 0:
            numero = (i+1)/i
        metadedepi *=numero
    pi = 2 * metadedepi
    return pi
    

    
