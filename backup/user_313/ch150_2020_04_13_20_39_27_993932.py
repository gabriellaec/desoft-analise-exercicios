import math
def calcula_pi (n):
    soma = 0
    for i in range(1,n+1):
        soma = soma + 6/(i**2)
    
    resultado = math.sqrt(soma)
    
    return resultado