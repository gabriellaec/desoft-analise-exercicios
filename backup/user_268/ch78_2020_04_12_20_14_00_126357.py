import math
def calcula_tempo(dic):
    dc = {}
    for i in dic:
        x = (200/dic[i]) ** (1/2)
        dc[i] = x
    return dc

cod = {}
n = input('nome')
a = float(input("aceleracao"))
while n != 'sair':
    cod[n] = a
    n = input('nome')
    if n != 'sair':
        a = float(input("aceleracao"))
    
temp = calcula_tempo(cod)
vlr = temp.values()
venc = min(vlr)

for i in temp:
    if temp[i] == venc:
        nome = i
print('O vencedor é {0} com tempo de conclusão de {1} s'.format(nome, venc))