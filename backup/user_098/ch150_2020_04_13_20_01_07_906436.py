def calcula_pi(n):
    somatorio = 0
    for i in range(n+1):
        if i == 0:
            somatorio += 0
        else:
            somatorio += 6/(i**2)
    return somatorio**(1/2)