def fatorial(n):
    i = 1
    produto = 1
    while i < n:
        produto = produto*(n - i + 1)
        i += 1
    return produto

numero_escolhido = 5

print(fatorial(numero_escolhido))