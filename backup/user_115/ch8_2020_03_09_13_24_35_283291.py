#s=f(t,s0,v)=s0+vt

def calcula_posicao(t,s0,v):
    s=s0+v*t
    return s

s0 = 0
v = 4
t = 15

print(calcula_posicao(t, s0, v))