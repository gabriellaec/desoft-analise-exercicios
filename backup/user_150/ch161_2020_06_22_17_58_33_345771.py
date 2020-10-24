def PiWallis(n):
    pi = 0
    i = 2
    z = 1
    while z <= n:
        pi += i / z
        if z != n:
            z += 2
            pi += i / z
            i += 2
        else:
            break

    return pi*2