def calcula_posicao(so,v,t):
           calcula_posicao= so+ v*t
           return calcula_posicao
so=input(float('diga a posição inicial'))
v=input(float('diga a velocidade'))
t=input(int('diga o tempo'))
print('para a posicao inicial {0}, a velocidade {1} e o tempo {2} temos a posicao final'.format(so,v,t,calcula_posicao))      