def calcula_pi(n):
    pi = 0
    i = 1
    while i <= n:
        pi = pi + (6/(i**2))
        i += 1
    raiz = (pi)**(1/2)
    return raiz