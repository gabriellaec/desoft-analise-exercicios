
def calcula_pi(n):
    soma = 0
    i = 1
    while i <= n:
        soma += (6/i**2)
        i = i + 1
    return (soma**(1/2))
        
   
