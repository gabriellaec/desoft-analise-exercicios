def calcula_pi(n):
    i = 1
    soma=0
    if n ==1:
        soma = 2.449489742783178
    while i<n:
        pi = (6/(i**2))**1/2
        soma +=pi
    return soma
        