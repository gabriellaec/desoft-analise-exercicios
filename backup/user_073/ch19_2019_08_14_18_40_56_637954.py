import math
def lancamento(v, y0, a):
    g=9.8
    θ=5/8
    A=(v**2)/(2*g)
    B=(1+((1+(2*g*y0)/(v**2*(math.sin(θ))**2))**0.5))
    d=A*B*math.sin(2*θ)
    return d
a=lancamento(2, 5, 6)
print(a)
