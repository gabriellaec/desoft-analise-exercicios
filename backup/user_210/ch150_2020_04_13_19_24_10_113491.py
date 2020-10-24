def calcula_pi(n):
    soma = 0
    for number in range(1, n+1):
        soma += 6/(number**2)
        
    return soma**0.5