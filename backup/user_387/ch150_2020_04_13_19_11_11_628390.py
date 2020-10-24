def calcula_pi(n):
    valor_pi = 0
    for n in range(1,n+1):
        valor_pi+=6/n**2
    valor_pi = valor_pi**0.5
    return valor_pi