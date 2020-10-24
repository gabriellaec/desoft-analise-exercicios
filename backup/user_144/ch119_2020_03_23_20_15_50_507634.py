def calcula_euler(x,n):
    i = 0
    soma = 0
    if i < n:
        cosh = x ** n / (n-1) * n
        soma += cosh
        i += 1
    return soma