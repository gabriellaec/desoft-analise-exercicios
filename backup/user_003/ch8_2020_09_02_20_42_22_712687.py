def calcula_posicao(s0,v,t):
    s = s0 + v * t
    return s
s0 = 0
v = 1
t = 7
s = calcula_posicao(s0,v,t)
print(s)