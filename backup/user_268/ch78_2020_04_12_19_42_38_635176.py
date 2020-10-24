import math
def calcula_tempo(dic):
    dc = {}
    for i in dic:
        x = (200/dic[i]) ** (1/2)
        dc[i] = x
    return dc



n = input('nome')
a = float(input("aceleracao")
di= {}
while n != 'sair':
    di[n] = a
    n = input('nome')
    a = float(input("aceleracao")
venc = min(calcula_tempo(di))
          