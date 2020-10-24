from math import radians, cos
A = int(input('Digite um valor em metros: ')
o = int(input('Digite um valor em graus: ')
w = int(input('Digite um valor em graus por segundo: ')
t = int(input('Digite um valor em segundos: ')
def calcula_elongacao(A,o,w,t):
    o = radians(o)
    w = radians(w)
    x = A*(cos(o+(w*t)))
    return x