def calcula_pi(n):
    i = 1
    soma = 0
    while i <= n:
        print(i)
        soma += 6/(i**2)
        i += 1
    return soma**0.5
