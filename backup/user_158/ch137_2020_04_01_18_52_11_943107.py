#importando biblioteca
import math
#definindo funcao
def calcula_aceleracao(r,f):
    F=f/60
    w=2*math.pi*F
    a=r*w**2
    return a