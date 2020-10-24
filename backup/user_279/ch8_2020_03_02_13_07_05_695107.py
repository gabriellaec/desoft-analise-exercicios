def calcula_posicao(s0,t,v):
    s=s0 + v * t
    return s

s0=0
t=10
v=5
y= calcula_posicao(s0,t,v)
print(y)