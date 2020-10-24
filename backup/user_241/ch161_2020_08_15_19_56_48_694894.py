def PiWallis(n):
    par = 2
    impar = 1
    pi_2 = par/impar
    i = 2
    while i <= n:
        if i % 2 == 0:
            impar += 2
        else:
            par += 2
        pi_2 = pi_2 * par/impar
        i += 1
    return 2 * pi_2