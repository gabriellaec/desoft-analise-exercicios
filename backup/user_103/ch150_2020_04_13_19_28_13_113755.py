def calcula_pi(n):
    exp=1
    soma = 0
    while exp <= n:
        soma+=6/exp**2
        exp+=1
    return soma**(1/2)