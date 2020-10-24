def calcula_pi(n):
    i=n
    soma=0
    while i>0:
        soma=soma+(6/i**2)
        i=i-1
    pi=(soma)**0.5
    return pi