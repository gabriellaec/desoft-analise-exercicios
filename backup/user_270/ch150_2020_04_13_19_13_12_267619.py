def calcula_pi(n):
    soma = 0
    for i in range(1,(n+1)):
        pi = 6/(n**2)
        soma += pi
    valor_pi = (soma)**(1/2)
    return valor_pi