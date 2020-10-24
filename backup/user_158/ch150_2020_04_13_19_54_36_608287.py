#importando Blibliotecas
import math

#definindo a funcao
def calcula_pi(n):
    i=1
    soma=0
    while i <= n:
        soma += 6/(i**2)
        i+=1
    pi = math.sqrt(soma)
    return pi
