
def calcula_posicao (s0,t,v):
    posicao_objeto= s0+v*t
    return posicao_objeto

s0=int(input(print("Dê a posição inicial:")))
v=int(input(print("Dê a velocidade:")))
t=int(input(print("Dê o tempo:")))
posicao_objeto=calcula_posicao(s0,t,v)
print(posicao_objeto)
