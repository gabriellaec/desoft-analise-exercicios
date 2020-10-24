
def calcula_posicao (s0,t,v):
    posicao_objeto= s0+v*t
    return posicao_objeto

s0=5
v=10
t=5
posicao_objeto=calcula_posicao(s0,t,v)
print(posicao_objeto)