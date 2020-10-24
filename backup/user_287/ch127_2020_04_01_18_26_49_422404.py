from math import radians, cos
def calcula_elongacao(A,ϕ0,w,t):
    ϕ0 = radians(ϕ0)
    w = radians(w)
    x = A*(cos(ϕ0+(w*t)))
    return x

    



