def calcula_pi (n):
    soma = 0
    numero = 1
    while numero - 1 < n:
        soma += 6 / (numero ** 2)
        numero += 1
    pi = soma ** 0.5
    return soma