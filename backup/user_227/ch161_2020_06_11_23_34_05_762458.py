def PiWallis(n):

    num = 2
    den = 1
    for elemento in range(n):
        if num % 2 == 0 and den % 2 != 0:
            pi_meios = num/den
        
        else:
            pi_meios = (num-1)/(den+1)

        den+=1
        num+=1

    pi = 2*pi_meios

    return pi