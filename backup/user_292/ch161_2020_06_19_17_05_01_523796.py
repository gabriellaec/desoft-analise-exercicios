def PiWallis(numero):
    m = 2
    n = 1
    c = 2/1
    for i in range(1,numero):
        if i % 2 == 0:
            m += 2
        else:
            n += 2
        c *= m/n
    pi = c*2
    return pi
