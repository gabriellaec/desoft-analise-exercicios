def calcula_pi(n):
    soma=0
    for i in range(1,n+1):
        parte=6/(i**2)
        soma+=parte
    pi=soma**(0.5)
    return pi