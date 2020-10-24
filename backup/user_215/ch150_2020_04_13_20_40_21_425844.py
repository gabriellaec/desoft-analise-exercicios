def calcula_pi(n):
    i = 1
    pi = 0
    while i <= n:
        pi += 6/(i**2)
        pi = pi ** 0.5
        i += 1
    return pi