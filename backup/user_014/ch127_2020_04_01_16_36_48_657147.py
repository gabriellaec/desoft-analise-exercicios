import math

#Sendo A a amplitude, f0 o ϕ0, om o ω e t o tempo
 
def calcula_elongacao (A, f0, om, t):
    x = A * (math.cos(math.radians(f0) + math.radians(om) * t))
    return x