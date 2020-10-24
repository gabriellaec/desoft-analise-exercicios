def calcula_pi(n):
    i = 1
    res = 0
    while i <= n:
        res += 6 / (i**2)
        i += 1
    resultado_final = res**(1/2)
    return resultado_final