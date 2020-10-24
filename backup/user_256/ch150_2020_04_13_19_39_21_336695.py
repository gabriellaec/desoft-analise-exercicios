def calcula_pi(n):
    i = 1
    soma=0
    if n==1:
        soma = 2.449489742783178
    while i<n:
        pi = 6/(i**2)
        soma +=pi**1/2
        i+=1
    return soma
        