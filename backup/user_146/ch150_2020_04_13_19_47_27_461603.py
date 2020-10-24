'''Esse código calcula o valor aproximado do numero irracional PI, e quanto maior for
o valor de 'n', mais próximo será o valor da função com o valor verdadeiro de PI
'''
import math 
def calcula_pi(n):
    x=1
    Y=0
    while x<= n:
        Y=Y+(6/x**2)
        x+=1
    resultado=math.sqrt(Pi)
    return resultado