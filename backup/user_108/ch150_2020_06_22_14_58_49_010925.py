def calcula_pi(n):
    return sum([6/(i+1)**2 for i in range(n)]) ** (1/2)