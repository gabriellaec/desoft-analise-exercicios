
def calcula_pi(n):
    i = 1
    soma = 0
    while 1 < n:
        pi = (6/(i**2))**(1/2)
        i += 1
        soma += pi
        return soma