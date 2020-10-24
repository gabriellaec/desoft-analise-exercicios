#importando Blibliotecas
import math

#definindo a funcao
def calcula_pi(n):
    i=0
    soma=0
    while i < n:
        soma += 6/(i**2)
    pi = math.sqrt(soma)
    return pi
