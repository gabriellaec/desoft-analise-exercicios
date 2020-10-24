def calcula_posicao(t,s0,v):
    s = s0 + v * t
    return s
s0 = 0
v = 1
t = 7
s = calcula_posicao(t,s0,v)
print(s)