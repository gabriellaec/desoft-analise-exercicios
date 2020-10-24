import math
def calcula_trabalho (x,y,z):
    t=x*math.cos (math.radians(y))*z
    return t
f=10
ang=60
s=2
resultado = calcula_trabalho (f,ang,s)
print (resultado)