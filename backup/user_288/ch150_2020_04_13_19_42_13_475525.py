def calcula_pi (n):
    soma = 0
    numero = 1
    while numero - 1 < n:
        conta = 6 / (numero ** 2)
        soma += conta
        numero += 1
    pi = soma ** 0.5
    return pi