def fatorial(n):
    produto = 1
    termos = range(1, n + 1)
    for i in termos:
        produto *= i
    return produto

print(fatorial(5))