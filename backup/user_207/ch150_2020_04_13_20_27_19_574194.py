def calcula_pi (n):
    somatorio = 0
    for i in range(1, n+1):
        somatorio += (6/(i**2))
        pi = (somatorio)**(0.5)
    return pi