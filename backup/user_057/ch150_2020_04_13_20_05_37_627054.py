def calcula_pi(N):
    x=0
    i=0
    while i < range(1, N):
        x = x + (6/(i*2))
        i += 1
    π = x*(1/2)
    return π