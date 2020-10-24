def calcula_pi(n):
    soma = list()
    for i in range(1, n+1):
        x = 6/(i**2)
        soma.append(x)
    pi = (sum(soma))**0.5
    return pi