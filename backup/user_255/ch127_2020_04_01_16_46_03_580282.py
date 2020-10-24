#Exercício 1 - Quiz
#A=amplitude do movimento (elongação máxima) (metros)
#t=tempo (segundos)
#ϕ0 = b =  em graus
#ω = w = em graus por segundo
#x = elongação no instante
import math
def calcula_angulo(b,w,t):
    angulo=(b+w*t)
    return angulo
angulo=calcula_angulo
print (angulo)
def calcula_elongacao(A,t,b,w):
    x=A*math.cos(math.radians(angulo))
    return x
x=calcula_elongacao
print(x)