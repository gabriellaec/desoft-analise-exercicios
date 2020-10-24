def fatorial(n):
    numero = 1
    multiplicacao = 1
    while numero <= n:
        multiplicacao *= numero
        numero += 1
    return multiplicacao

def calcula_euler(x, n):
    soma = 1 + x
    for i in range(2, n):
        soma += (x**i) / fatorial(i)
    return soma