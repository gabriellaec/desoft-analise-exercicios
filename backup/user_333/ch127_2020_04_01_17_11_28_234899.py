import math

#a função recebe os valores da amplitude do movimento(A), a fase inicial(finicial), a velocidade angular(vangular) e o tempo
#retorna a posição x em função de t
def calcula_elongacao(A,finicial,vangular,t):
    parenteses_em_rad=math.radians(finicial+vangular*t) #cálculo separado para facilitar transformações
    x=A*math.cos(parenteses_em_rad)
    return x
    