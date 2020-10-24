def calcula_pi(n):
    i=0
    soma = 0
    while i <= n:
        x = 6/(i**2)
        soma += x
        i+=1
    resultado = soma**(0.5)
    return resultado