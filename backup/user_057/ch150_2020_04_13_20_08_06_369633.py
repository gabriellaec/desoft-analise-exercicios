def calcula_pi(N):
    x=0
    for i in range(1, (N+1)):
        x = x + (6/(i*2))
    π = x*(1/2)
    return π