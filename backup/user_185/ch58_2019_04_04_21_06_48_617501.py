def calcula_fibonacci(n):
    F[0] = 1
    F[1] = 1
    contador = 2
    soma = 0
    while contador < n:
        soma = soma + F[contador]
    return soma
        
        
        